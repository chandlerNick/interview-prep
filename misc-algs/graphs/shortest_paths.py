import heapq
import math
import random

import heapq
import math

class ShortestPath:
    def __init__(self, graph: dict):
        """graph: {u: [(v, weight), ...]}"""
        self.graph = graph

    def _reconstruct_path(self, predecessors, start, goal):
        path = []
        curr = goal
        while curr is not None:
            path.append(curr)
            if curr == start: break
            curr = predecessors.get(curr)
        return path[::-1] if path[-1] == start else []

    def dijkstra(self, start_node, goal_node=None):
        distances = {node: float('inf') for node in self.graph}
        predecessors = {node: None for node in self.graph}
        distances[start_node] = 0
        pq = [(0, start_node)]

        while pq:
            curr_d, u = heapq.heappop(pq)
            if curr_d > distances[u]: continue
            if u == goal_node: break

            for v, weight in self.graph.get(u, []):
                dist = curr_d + weight
                if dist < distances[v]:
                    distances[v] = dist
                    predecessors[v] = u
                    heapq.heappush(pq, (dist, v))
        
        return distances, predecessors

    def bellman_ford(self, start_node, num_nodes):
        distances = {i: float('inf') for i in range(num_nodes)}
        predecessors = {i: None for i in range(num_nodes)}
        distances[start_node] = 0
        
        for _ in range(num_nodes - 1):
            for u in self.graph:
                for v, weight in self.graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        predecessors[v] = u

        for u in self.graph:
            for v, weight in self.graph[u]:
                if distances[u] + weight < distances[v]:
                    raise ValueError("Negative weight cycle detected!")

        return distances, predecessors

    def a_star(self, start_node, goal_node, coords):
        def h(u):
            return math.dist(coords[u], coords[goal_node])

        pq = [(h(start_node), 0, start_node)]
        g_scores = {node: float('inf') for node in self.graph}
        predecessors = {node: None for node in self.graph}
        g_scores[start_node] = 0
        
        while pq:
            f, g, u = heapq.heappop(pq)
            if u == goal_node: break

            for v, weight in self.graph.get(u, []):
                tentative_g = g + weight
                if tentative_g < g_scores[v]:
                    g_scores[v] = tentative_g
                    predecessors[v] = u
                    heapq.heappush(pq, (tentative_g + h(v), tentative_g, v))

        return g_scores, predecessors


from graph_gen import generate_weighted_connected_graph
from shortest_paths import ShortestPath
from viz import visualize_search

if __name__ == "__main__":
    N = 8
    start, goal = 0, N-1
    adj = generate_weighted_connected_graph(N, extra_edges=10)
    solver = ShortestPath(adj)

    print(f"--- Shortest Path Results (Source: {start}, Goal: {goal}) ---")

    # Dijkstra
    dists, prevs = solver.dijkstra(start)
    path = solver._reconstruct_path(prevs, start, goal)
    print(f"Dijkstra: Path {path} | Cost: {dists[goal]}")

    # Bellman-Ford
    try:
        bf_dists, bf_prevs = solver.bellman_ford(start, N)
        bf_path = solver._reconstruct_path(bf_prevs, start, goal)
        print(f"Bellman-Ford: Path {bf_path} | Cost: {bf_dists[goal]}")
    except ValueError as e:
        print(f"Bellman-Ford: {e}")

    # A*
    coords = {i: (random.randint(0, 50), random.randint(0, 50)) for i in range(N)}
    as_dists, as_prevs = solver.a_star(start, goal, coords)
    as_path = solver._reconstruct_path(as_prevs, start, goal)
    print(f"A* Search: Path {as_path} | Cost: {as_dists[goal]}")