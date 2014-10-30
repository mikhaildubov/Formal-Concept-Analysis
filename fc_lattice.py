def lattice(concepts):
    """Computes formal concepts lattice.

    :param concepts: List of concept tuples, as returned by the compute_fc() methods
    :returns: List of lattice edges, each edge being a pair (C1, C2),
              where C1 and C2 are concept tuples
    """
    concepts_sorted = sorted(concepts, key=lambda x: len(x[0]))
    edges = []
    for c1 in concepts_sorted:
        c1_adj = []
        for c2 in concepts_sorted:
            if c1[0] < c2[0]:
                for c_adj in c1_adj:
                    if c_adj[0] < c2[0]:
                        break
                else:
                    c1_adj.append(c2)
        for c2 in c1_adj:
            edges.append((c1, c2))
    return edges
