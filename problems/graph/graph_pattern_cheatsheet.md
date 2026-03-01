# Graph Pattern Cheat Sheet (Interview Recognition)

Use this as a fast decision map when you read a problem.

## 1) BFS
- **Use when:** shortest path in an **unweighted** graph (or all edges weight = 1), level-order expansion, minimum number of steps.
- **Signals:** "minimum moves", "fewest edges", grid with 4/8-direction unit moves.
- **Core idea:** explore layer by layer from source.
- **Complexity:** `O(V + E)`.

## 2) Dijkstra
- **Use when:** shortest path with **non-negative weighted** edges.
- **Signals:** minimum cost/time/effort in weighted graph/grid.
- **Core idea:** min-heap over current best distance; relax neighbors.
- **Do not use when:** negative edge weights exist.
- **Complexity:** `O((V + E) log V)` with heap.

## 3) Topological Sort (Kahn / DFS)
- **Use when:** dependency ordering in a **DAG**.
- **Signals:** prerequisites, build order, scheduling with constraints.
- **Core idea:** process nodes with indegree 0 (Kahn) or DFS postorder.
- **Cycle meaning:** no valid ordering.
- **Complexity:** `O(V + E)`.

## 4) Union-Find (DSU)
- **Use when:** dynamic connectivity, components, cycle detection in undirected edges.
- **Signals:** "are these connected?", "add edges", "count components".
- **Core idea:** merge sets + find representative.
- **Complexity:** near-constant amortized per op, `O(alpha(N))`.

## 5) Euler Path / Cycle (Hierholzer)
- **Use when:** must use **every edge exactly once**.
- **Signals:** "use every ticket/road/pair exactly once", reconstruct full edge traversal.
- **Core idea:** walk edges, remove as used, append node when stuck (postorder), reverse route.
- **Directed degree rules:**
  - Trail: one node `out-in = 1` (start), one node `in-out = 1` (end), others balanced.
  - Cycle: all nodes balanced (`in == out`), start anywhere with outgoing edge.
- **Complexity:** `O(E)` traversal (+ sorting if lexicographic order needed).

## 6) Minimum Spanning Tree (Kruskal / Prim)
- **Use when:** connect all nodes with minimum total edge cost (not shortest path between two nodes).
- **Signals:** "minimum cost to connect all cities/points".
- **Core idea:** pick cheapest edges without creating cycles.

## 7) DFS Backtracking (Path Existence / Enumeration)
- **Use when:** need to explore possibilities, validate constraints, or enumerate paths.
- **Signals:** "can we reach", "all paths", "word search", constraint-heavy path building.
- **Core idea:** choose, recurse, undo.

## 8) Bellman-Ford / SPFA-style
- **Use when:** shortest path with possible **negative weights**.
- **Signals:** negative edges, detect negative cycle.
- **Core idea:** repeated relaxation across all edges.
- **Complexity:** Bellman-Ford `O(VE)`.

## Quick Decision Flow
1. **"Every edge exactly once"?** -> Euler (Hierholzer).
2. **"Dependencies / ordering"?** -> Topological sort.
3. **"Connectivity under unions"?** -> DSU.
4. **"Shortest path"?**
   - Unweighted -> BFS
   - Weighted non-negative -> Dijkstra
   - Negative edges -> Bellman-Ford
5. **"Connect all nodes with minimum total cost"?** -> MST.

## Interview Sound Bites
- "This is not shortest path; this is edge-exactly-once, so Euler trail."
- "Weights are non-negative, so Dijkstra is safe."
- "Prerequisite constraints imply DAG ordering, so topological sort."
- "This is connectivity with incremental unions, so DSU."

## Common Pitfalls
- Using BFS on weighted graph (wrong unless all weights equal).
- Using Dijkstra with negative weights.
- Confusing MST with shortest path.
- In Euler problems, building output while walking (instead of postorder + reverse).
- Forgetting stale heap entries in Dijkstra (`if d > dist[u]: continue`).
