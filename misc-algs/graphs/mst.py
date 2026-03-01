import heapq
from dsu import DSU

class MSTAlgorithms:
    def __init__(self, graph: dict):
        self.graph = graph

    def prims(self, start_node=0):
        """
        Computes the MST using Prim's Algorithm.
        Returns: (list of edges in MST, total weight)
        """
        mst_edges = []
        visited = {start_node}
        total_weight = 0
        
        # Priority Queue stores: (weight, from_node, to_node)
        # We start by adding all edges from the start_node
        edges = [
            (weight, start_node, neighbor) 
            for neighbor, weight in self.graph.get(start_node, [])
        ]
        heapq.heapify(edges)

        while edges:
            weight, u, v = heapq.heappop(edges)
            
            if v not in visited:
                visited.add(v)
                mst_edges.append((u, v, weight))
                total_weight += weight
                
                # Add new edges from the newly visited node v
                for next_neighbor, next_weight in self.graph.get(v, []):
                    if next_neighbor not in visited:
                        heapq.heappush(edges, (next_weight, v, next_neighbor))
                        
        return mst_edges, total_weight
    
    def kruskals(self):
        """
        Computes MST by sorting all edges by weight and 
        adding them if they don't form a cycle.
        """
        num_nodes = len(self.graph)
        edges = []
        
        # Flatten the adjacency list into a unique list of edges
        for u in self.graph:
            for v, weight in self.graph[u]:
                if u < v: # Ensure we don't add (u,v) and (v,u)
                    edges.append((weight, u, v))
        
        # Greedy Step: Sort edges by weight
        edges.sort()
        
        dsu = DSU(num_nodes)
        mst_edges = []
        total_weight = 0
        
        for weight, u, v in edges:
            if dsu.union(u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight
                
        return mst_edges, total_weight


if __name__ == "__main__":
    from graph_gen import generate_weighted_connected_graph
    from viz import visualize_mst

    # 10 nodes, 15 extra edges to ensure a dense graph
    weighted_adj = generate_weighted_connected_graph(10, 15)
    
    solver = MSTAlgorithms(weighted_adj)
    mst_path, weight = solver.prims(0)
    
    print(f"Total MST Weight: {weight}")
    print(f"MST Edges: {mst_path}")
    
    visualize_mst(weighted_adj, mst_path)

   
    
    print("--- Kruskal's MST Algorithm ---")
    mst, cost = solver.kruskals()
    
    print(f"Total MST Cost: {cost}")
    print("Edges in MST:")
    print("source -- (weight) -- sink")
    for u, v, w in mst:
        print(f"  {u} --({w})-- {v}")

    # To verify connectivity, an MST should always have N-1 edges
    assert len(mst) == 9
    print("\nVerification: MST contains N-1 edges. Connectivity confirmed.")