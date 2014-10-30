def compute_fc(ctx):
    """Computes formal concepts using the Close-by-One (CbO) algorithm [Kuznetsov].

    The algorithm has the |G||M|^2|L| complexity, where L is the resulting set of concepts.

    :param ctx: Context object
    :returns: List of concepts, each concept being a pair (A, B),
              where A <= G, B <= G
    """
    res = []
    G_sorted = sorted(list(ctx.G))
    G_index = {g:i for (i, g) in enumerate(G_sorted)}
    # NOTE(msdubov): Testing the degenerate concept separately
    if ctx.is_fc(set()):
        res.append((set(), ctx.G_prime(set())))
    def cbo(prefix):
        # Prevent non-canonical intents by starting with the next element
        subtree_start = G_index[prefix[-1]] + 1 if prefix else 0
        for start in range(subtree_start, len(G_sorted)):
            i = start
            next = prefix + [G_sorted[i]]
            while not ctx.is_fc(set(next)) and i < len(G_sorted) - 1:
                i += 1
                next.append(G_sorted[i])
            if ctx.is_fc(set(next)):
                g = set(next)
                res.append((g, ctx.G_prime(g)))
                cbo(next)
    cbo([])
    return res
