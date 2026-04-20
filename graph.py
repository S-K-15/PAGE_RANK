import networkx as nx

def create_web_graph():
    G = nx.DiGraph()

    pages = ['A', 'B', 'C', 'D', 'E', 'F']
    G.add_nodes_from(pages)

    links = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'),
        ('C', 'B'), ('C', 'D'), ('C', 'E'),
        ('D', 'A'),
        ('E', 'F'),
        ('F', 'A'), ('F', 'B')
    ]
    G.add_edges_from(links)

    return G