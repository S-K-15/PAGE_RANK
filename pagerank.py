import numpy as np

def power_iteration_pagerank(G, damping=0.85, max_iterations=100, tolerance=1e-6):
    pages = list(G.nodes())
    n = len(pages)
    index = {page: i for i, page in enumerate(pages)}
    rank = np.ones(n) / n
    history = []

    for _ in range(max_iterations):
        old_rank = rank.copy()
        new_rank = np.zeros(n)

        for i, page in enumerate(pages):
            incoming = list(G.predecessors(page))
            s = 0
            for inc in incoming:
                j = index[inc]
                out_links = G.out_degree(inc)
                if out_links > 0:
                    s += old_rank[j] / out_links

            new_rank[i] = (1 - damping)/n + damping*s

        error = np.sum(np.abs(new_rank - old_rank))
        history.append(error)
        rank = new_rank

        if error < tolerance:
            break

    return {pages[i]: rank[i] for i in range(n)}, history


def gauss_seidel_pagerank(G, damping=0.85, max_iterations=100, tolerance=1e-6):
    pages = list(G.nodes())
    n = len(pages)
    index = {page: i for i, page in enumerate(pages)}
    rank = np.ones(n) / n
    history = []

    for _ in range(max_iterations):
        old_rank = rank.copy()

        for i, page in enumerate(pages):
            incoming = list(G.predecessors(page))
            s = 0
            for inc in incoming:
                j = index[inc]
                out_links = G.out_degree(inc)
                if out_links > 0:
                    s += rank[j] / out_links

            rank[i] = (1 - damping)/n + damping*s

        error = np.sum(np.abs(rank - old_rank))
        history.append(error)

        if error < tolerance:
            break

    return {pages[i]: rank[i] for i in range(n)}, history