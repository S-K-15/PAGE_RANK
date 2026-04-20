import streamlit as st

from graph import create_web_graph
from pagerank import power_iteration_pagerank, gauss_seidel_pagerank
from visualize import draw_graph, draw_convergence

st.set_page_config(page_title="PageRank Visualizer", layout="wide")

st.title("🔗 PageRank Algorithm Visualizer")

# Sidebar controls
st.sidebar.header("⚙️ Controls")

algorithm = st.sidebar.selectbox(
    "Algorithm",
    ["Power Iteration", "Gauss-Seidel"]
)

damping = st.sidebar.slider("Damping", 0.5, 0.95, 0.85)
max_iter = st.sidebar.number_input("Max Iterations", 10, 200, 50)
tolerance = st.sidebar.number_input("Tolerance", value=1e-6, format="%.6f")

run = st.sidebar.button("▶ Run")

if run:
    G = create_web_graph()

    if algorithm == "Power Iteration":
        ranks, history = power_iteration_pagerank(G, damping, max_iter, tolerance)
    else:
        ranks, history = gauss_seidel_pagerank(G, damping, max_iter, tolerance)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Graph")
        st.pyplot(draw_graph(G, ranks))

    with col2:
        st.subheader("Rankings")
        sorted_ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)

        for i, (node, score) in enumerate(sorted_ranks, 1):
            st.write(f"Rank {i} — {node} — {score:.4f}")
            st.progress(float(score))

    st.subheader("Convergence")
    st.pyplot(draw_convergence(history))

    st.success(f"Converged in {len(history)} iterations")