import sys

import fc_cbo
import fc_context
import fc_lattice

def main():
    ctx = fc_context.Context(sys.argv[1])
    formal_concepts = fc_cbo.compute_fc(ctx)
    lattice = fc_lattice.lattice(formal_concepts)
    print len(lattice)

if __name__ == '__main__':
    main()
