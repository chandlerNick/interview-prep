# Nick Chandler - 01.03.2026

import random
from collections import defaultdict

def generate_random_graph(num_nodes: int, edges_per_node: int, directed: bool = False) -> dict:
	"""Generates an adjacency list representation of a graph"""
	graph = defaultdict(list)
	for i in range(num_nodes):
		# Prevent self-loops
		targets = random.sample([n for n in range(num_nodes) if n != i], edges_per_node)
		for t in targets:
			graph[i].append(t)
			if not directed:
				graph[t].append(i)
		
		if not directed:
			# Dedup
			for k in graph:
				graph[k] = list(set(graph[k]))
		
		return dict(graph)
	
import random
from collections import defaultdict

def generate_connected_graph(num_nodes: int, extra_edges: int = 0) -> dict:
    """Guarantees a single connected component using a spanning tree approach."""
    if num_nodes < 1: return {}
    
    adj = {i: set() for i in range(num_nodes)}
    nodes = list(range(num_nodes))
    
    # 1. Create a Spanning Tree
    connected = {nodes[0]}
    remaining = set(nodes[1:])
    
    while remaining:
        u = random.choice(list(connected))
        v = random.choice(list(remaining))
        
        adj[u].add(v)
        adj[v].add(u)
        
        remaining.remove(v)
        connected.add(v)
        
    # 2. Add extra edges for complexity
    potential_edges = [(i, j) for i in range(num_nodes) for j in range(i + 1, num_nodes) 
                       if j not in adj[i]]
    
    actual_extras = min(len(potential_edges), extra_edges)
    for u, v in random.sample(potential_edges, actual_extras):
        adj[u].add(v)
        adj[v].add(u)
        
    return {k: list(v) for k, v in adj.items()}



def generate_weighted_connected_graph(num_nodes: int, extra_edges: int = 0, weight_range: tuple = (1, 10)) -> dict:
    """Guarantees a connected graph where edges have random weights."""
    if num_nodes < 1: return {}
    
    adj = {i: [] for i in range(num_nodes)}
    nodes = list(range(num_nodes))
    
    connected = {nodes[0]}
    remaining = set(nodes[1:])
    
    while remaining:
        u = random.choice(list(connected))
        v = random.choice(list(remaining))
        weight = random.randint(*weight_range)
        
        adj[u].append((v, weight))
        adj[v].append((u, weight))
        
        remaining.remove(v)
        connected.add(v)
        
    # Add extra random edges
    for _ in range(extra_edges):
        u, v = random.sample(nodes, 2)
        # Check if edge already exists to keep it simple
        if v not in [edge[0] for edge in adj[u]]:
            weight = random.randint(*weight_range)
            adj[u].append((v, weight))
            adj[v].append((u, weight))
            
    return adj

