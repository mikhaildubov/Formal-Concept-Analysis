class Context(object):

    def __init__(self, filepath):
        """Initializes the context from a .cxt file.

        :param filepath: Path to a file in .cxt format
        """
        with open(filepath) as f:
            lines = f.read().splitlines()
        self.name = lines[1]
        G_size = int(lines[2])
        M_size = int(lines[3])
        G_list = lines[4:(4 + G_size)]
        M_list = lines[(4 + G_size):(4 + G_size + M_size)]
        self.G = set(G_list)
        self.M = set(M_list)
        table_start = 4 + G_size + M_size
        self.ctx = {}
        for i in xrange(G_size):
            table_line = lines[table_start + i]
            for j in xrange(M_size):
                self.ctx[(G_list[i], M_list[j])] = (table_line[j] == "X")

    def G_prime(self, A):
        """Computes A'.

        :param A: subset of objects A <= G
        :returns: subset of features A' <= M
        """
        res = set()
        for m in self.M:
            if all(self.ctx[(a, m)] for a in A):
                res.add(m)
        return res

    def M_prime(self, A):
        """Computes B'.

        :param B: subset of objects B <= M
        :returns: subset of features B' <= G
        """
        res = set()
        for g in self.G:
            if all(self.ctx[(g, a)] for a in A):
                res.add(g)
        return res

    def is_fc(self, A):
        """Checks that the given subset of objects A <= M forms a concept.

        Checks that A'' = A.

        :param A: subset of objects A <= G
        :returns: True if (A, A') is a concept, False otherwise
        """
        return self.M_prime(self.G_prime(A)) == A
