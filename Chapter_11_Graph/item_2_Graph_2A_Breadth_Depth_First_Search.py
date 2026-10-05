# ================================================================================
# Chapter 11 - Item 2: Graph-2A Breadth/Depth First Search
# --------------------------------------------------------------------------------
# Problem Statement:
# Graph traversal visits every vertex of a graph exactly once. Build the graph
# from comma-separated edges and print both traversals:
# - Depth-First Search (DFS): go as deep as possible, then backtrack (stack).
# - Breadth-First Search (BFS): visit level by level from the start (queue).
#
# Inputs:
# - Comma-separated edges "<u> <v>", e.g. 1 2, 1 3, 1 5, 3 4, 4 3
# Outputs:
# - "Depth First Traversals : <vertices>"
# - "Bredth First Traversals : <vertices>"  (spelling as on the portal)
# ================================================================================

from collections import deque

def dfs(graph, vertices):
    visited, order = set(), []

    def visit(u):
        visited.add(u)
        order.append(u)
        for v in graph[u]:
            if v not in visited:
                visit(v)

    # Restart from every unvisited vertex so disconnected parts are covered
    for s in vertices:
        if s not in visited:
            visit(s)
    return order

def bfs(graph, vertices):
    visited, order = set(), []
    for s in vertices:
        if s in visited:
            continue
        visited.add(s)
        queue = deque([s])
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
    return order

def solve():
    print(" *** Graph Traversal ***")
    edges = [e.split() for e in input("Enter : ").split(",") if e.strip()]

    # The expected outputs treat each edge as two-way, neighbours in sorted order
    vertices = sorted({v for edge in edges for v in edge})
    graph = {v: set() for v in vertices}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    graph = {v: sorted(n) for v, n in graph.items()}

    print("Depth First Traversals :", *dfs(graph, vertices))
    print("Bredth First Traversals :", *bfs(graph, vertices))
    print("===== End of program =====")

if __name__ == '__main__':
    solve()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# 1. Parse the edges and build an adjacency list. Each edge is stored both ways
#    and each neighbour list is sorted, so the traversal order is deterministic.
# 2. DFS: recursive visit() marks a vertex, records it, then dives into each
#    unvisited neighbour before trying the next one.
# 3. BFS: a deque holds the frontier; a vertex is marked when enqueued, so it is
#    never queued twice, and vertices come out level by level.
# 4. Both start from the smallest vertex and restart from any vertex still
#    unvisited, so every vertex appears exactly once.
#
# Worked example -- Enter : a b, b c, d e, e a, c e
#   neighbours: a[b,e] b[a,c] c[b,e] d[e] e[a,c,d]
#   DFS: a -> b -> c -> e -> d            => a b c e d
#   BFS: a | b e | c d                    => a b e c d
# ================================================================================
