from itertools import chain, combinations

def powerset(S):
    """Return a powerset generator for the given set.

    :param S: set object
    :returns: generator of sets
    """
    for subset in chain.from_iterable(combinations(S, r) for r in range(len(S) + 1)):
        yield set(subset)

def compute_fc(ctx):
    """Computes formal concepts using a Naive algorithm.

    The algorithm has exponential 2^|G| complexity.

    :param ctx: Context object
    :returns: List of concepts, each concept being a pair (A, B),
              where A <= G, B <= G
    """
    fc = []
    for g in powerset(ctx.G):
        m = ctx.G_prime(g)
        if ctx.M_prime(m) == g:
            fc.append((g, m))
    return fc
