# ================================================================================
# Chapter 11 - Item 1: Graph-1A (Directed Graph Adjacency Matrix)
# --------------------------------------------------------------------------------
# Problem Statement:
# Write a Python code to accept a string of comma-separated directed edges and
# display the adjacency matrix of the directed graph.
#
# Inputs:
# - Comma-separated edges "<from> <to>", e.g. 1 2, 1 3, 1 5, 3 4, 4 3
# Outputs:
# - A header row of the sorted vertices, then one row per vertex
#   "<vertex> : <0/1 for each column>" where 1 means an edge row -> column.
# ================================================================================

def solve():
    print(" *** Directed Graph Adjacency Matrix ***")
    edges = [e.split() for e in input("Enter : ").split(",") if e.strip()]

    # Rows and columns use the vertices in sorted order
    vertices = sorted({v for edge in edges for v in edge})
    index = {v: i for i, v in enumerate(vertices)}

    matrix = [[0] * len(vertices) for _ in vertices]
    for u, v in edges:
        matrix[index[u]][index[v]] = 1

    print("    " + "  ".join(vertices))
    for v, row in zip(vertices, matrix):
        print(f"{v} : " + ", ".join(map(str, row)))
    print("===== End of program ======")

if __name__ == '__main__':
    solve()

# ================================================================================
# How it works:
# --------------------------------------------------------------------------------
# 1. Split the input on "," and each edge on whitespace -> [from, to] pairs
#    (stray spaces such as "A B,B C" vs "1 2, 1 3" are handled by split()).
# 2. Collect every vertex into a set and sort it; map each vertex to its index.
# 3. Build an n x n matrix of zeros and set matrix[from][to] = 1 per edge.
#    Direction matters: only the row of the source vertex is marked.
# 4. Print the header (4 spaces, vertices joined by 2 spaces), then each row.
#
# Worked example -- Enter : 1 2, 1 3, 1 5, 3 4, 4 3
#   vertices = [1, 2, 3, 4, 5]
#   row 1 has edges to 2, 3, 5 -> 0, 1, 1, 0, 1
#   row 3 -> 4 and row 4 -> 3 -> a 2-cycle, rows 2 and 5 are all zeros.
# ================================================================================
