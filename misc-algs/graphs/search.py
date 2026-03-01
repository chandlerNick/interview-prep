from collections import deque
from graph_gen import generate_random_graph, generate_connected_graph
from viz import visualize_search

class GraphSearch:
    def __init__(self, graph: dict):
        self.graph = graph
    
    def _generic_search(self, start_node, frontier, push_func, pop_func):
        # Map: node -> distance from start_node
        distances = {start_node: 0} 
        traversal_order = []
        
        # We push a tuple (node, current_dist)
        push_func(frontier, (start_node, 0))

        while frontier:
            node, dist = pop_func(frontier)
            traversal_order.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in distances:
                    distances[neighbor] = dist + 1
                    push_func(frontier, (neighbor, dist + 1))
                    
        return traversal_order, distances
    
    def bfs(self, start_node):
        queue = deque()
        order, dists = self._generic_search(
            start_node, queue, 
            lambda q, item: q.append(item), 
            lambda q: q.popleft()
        )
        return order, dists

    def dfs(self, start_node):
        stack = []
        order, dists = self._generic_search(
            start_node, stack, 
            lambda s, item: s.append(item), 
            lambda s: s.pop()
        )
        return order, dists

if __name__ == "__main__":
    # Generate a sparse graph with 6 nodes
    adj_list = generate_connected_graph(num_nodes=8, extra_edges=20)    
    print(f"Graph: {adj_list}")

    searcher = GraphSearch(adj_list)
    
    # Assuming node 0 exists
    b_order, b_dists = searcher.bfs(0)
    d_order, _ = searcher.dfs(0)
    print(f"BFS Order: {b_order} BFS dists: {b_dists}")
    print(f"DFS Order: {d_order}")
    
    
    num_nodes = 12
    adj_list = generate_connected_graph(num_nodes=num_nodes, extra_edges=10)    
    searcher = GraphSearch(adj_list)
    
    # Run BFS
    b_order, b_dists = searcher.bfs(0)
    visualize_search(adj_list, b_order, b_dists, title="BFS: Distance and Order", filename="bfs_viz.png")
    
    # Run DFS 
    d_order, d_dists = searcher.dfs(0)
    visualize_search(adj_list, d_order, d_dists, title="DFS: Depth and Order", filename="dfs_viz.png")