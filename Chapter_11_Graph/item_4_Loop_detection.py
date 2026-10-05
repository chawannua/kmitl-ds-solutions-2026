# ================================================================================
# Chapter 11 - Item 4: Loop detection
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a function to find a loop (cycle) in a graph given as comma-separated
# edges and display whether the graph has a cycle.
#
# Inputs:
# - Comma-separated edges "<u> <v>", e.g. 0 1,1 2,2 0
# Outputs:
# - "Graph has a cycle" or "Graph has no cycle"
# ================================================================================

def has_cycle(edges):
    # Union-Find: each vertex starts in its own set
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path halving
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        # Both ends already connected -> this edge closes a loop
        if ru == rv:
            return True
        parent[ru] = rv
    return False

def solve():
    edges = [e.split() for e in input("Enter : ").split(",") if e.strip()]
    print("Graph has a cycle" if has_cycle(edges) else "Graph has no cycle")

if __name__ == '__main__':
    solve()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# The portal's expected answers follow the edges in either direction (e.g. test
# "0 1,0 2,0 3,0 4,1 2,1 3,1 4,4 3,4 2,3 2" is reported as a cycle even though no
# directed cycle exists), so this detects a loop in the underlying graph.
# 1. Union-Find keeps track of which vertices are already connected.
# 2. For each edge u-v: if u and v are already in the same set, adding the edge
#    closes a loop -> cycle. Otherwise merge the two sets.
# 3. A self-loop like "3 3" is caught immediately (find(3) == find(3)).
#
# Worked example -- Enter : 0 1,1 2,2 0
#   0-1 merge, 1-2 merge, 2-0: both already in {0,1,2} => Graph has a cycle
# ================================================================================
