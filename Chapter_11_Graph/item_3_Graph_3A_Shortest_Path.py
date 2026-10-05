# ================================================================================
# Chapter 11 - Item 3: Graph-3A Shortest Path
# --------------------------------------------------------------------------------
# Problem Statement:
# Take input as a list of ordered pairs to construct a weighted directed graph.
# Then, display the shortest path using Dijkstra's Shortest Path Algorithm.
#
# Inputs:
# - "<edges>/<queries>"
#   edges   : "source weight destination" separated by commas
#   queries : "start target" separated by commas
#   e.g. v0 1 v1,v1 1 v2,v2 1 v3,v0 1 v3/v0 v1,v0 v2,v0 v3
# Outputs:
# - "<start> to <target> : <v1->v2->...>" for each query, or
# - "Not have path : <start> to <target>" when the target is unreachable.
# ================================================================================

import heapq

def dijkstra(graph, start):
    # dist[v] = best known distance from start, prev[v] = vertex before v
    dist = {start: 0}
    prev = {start: None}
    heap = [(0, start)]
    done = set()
    while heap:
        d, u = heapq.heappop(heap)
        if u in done:
            continue
        done.add(u)
        for w, v in graph.get(u, []):
            if v not in dist or d + w < dist[v]:
                dist[v] = d + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))
    return prev

def solve():
    print(" *** Shortest Path (Dijkstra's Algorithm) ***")
    edge_part, query_part = input("Enter : ").split("/")

    graph = {}
    for item in edge_part.split(","):
        if item.strip():
            u, w, v = item.split()
            graph.setdefault(u, []).append((float(w), v))

    for item in query_part.split(","):
        if not item.strip():
            continue
        start, target = item.split()
        prev = dijkstra(graph, start)
        if target not in prev:
            print(f"Not have path : {start} to {target}")
            continue
        # Walk the prev links back from the target, then reverse
        path = []
        while target is not None:
            path.append(target)
            target = prev[target]
        print(f"{start} to {path[0]} : " + "->".join(reversed(path)))

if __name__ == '__main__':
    solve()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# 1. Split the input on "/". The left side becomes an adjacency list
#    graph[u] = [(weight, v), ...]; the right side is the list of queries.
# 2. Dijkstra from each query's start: pop the closest unfinished vertex from a
#    min-heap, finalize it, and relax its outgoing edges, remembering prev[v]
#    whenever a strictly shorter distance is found.
# 3. If the target never got a distance it is unreachable -> "Not have path".
#    Otherwise follow prev[] back to the start and print the reversed path.
#
# Worked example -- Enter : v0 2 v1,v0 1 v3,...,v6 1 v5/v0 v5
#   v0 -> v3 (1) -> v6 (5) -> v5 (6) beats v0 -> v3 -> v5 (9)
#   => v0 to v5 : v0->v3->v6->v5
# ================================================================================
