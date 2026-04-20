import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(G, ranks):
    pos = nx.spring_layout(G, seed=42)

    sizes = [ranks[n]*10000 for n in G.nodes()]
    colors = [ranks[n] for n in G.nodes()]

    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True,
            node_size=sizes,
            node_color=colors,
            cmap=plt.cm.YlOrRd,
            ax=ax)
    return fig


def draw_convergence(history):
    fig, ax = plt.subplots()
    ax.plot(history, marker='o')
    ax.set_yscale('log')
    ax.set_title("Convergence")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Error")
    return fig