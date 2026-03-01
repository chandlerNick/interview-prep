import networkx as nx
import matplotlib.pyplot as plt

def visualize_search(adj_list, traversal_order, distances, title="Graph Traversal", filename="graph_output.png"):
    """
    Visualizes the graph:
    - Node Labels: Node ID (Distance)
    - Node Color: Position in traversal_order (darker = later)
    """
    # Create NetworkX graph
    G = nx.Graph(adj_list)
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(12, 8))
    
    # Create labels using the distances dict: e.g., "0 (d:0)"
    labels = {node: f"{node}\n(d:{distances.get(node, '∞')})" for node in G.nodes()}
    
    # Create color map based on index in traversal_order
    # Nodes not in traversal_order get a default light gray
    node_colors = []
    for node in G.nodes():
        if node in traversal_order:
            node_colors.append(traversal_order.index(node))
        else:
            node_colors.append(-1)

    # Draw the graph
    nodes = nx.draw_networkx_nodes(
        G, pos, 
        node_color=node_colors, 
        cmap=plt.cm.Blues, 
        node_size=800, 
        edgecolors='black'
    )
    
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=9, font_weight='bold')

    plt.title(title)
    plt.colorbar(nodes, label="Traversal Step Index")
    plt.axis('off')
    
    plt.savefig(filename)
    print(f"Visualization saved to {filename}")
    plt.close()

def visualize_mst(adj_list, mst_edges, title="Prim's MST"):
    G = nx.Graph()
    # Add all edges from adj_list
    for u, neighbors in adj_list.items():
        for v, w in neighbors:
            G.add_edge(u, v, weight=w)
            
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 7))
    
    # Draw all edges faintly
    nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color='gray')
    
    # Highlight MST edges
    mst_g = nx.Graph()
    mst_g.add_weighted_edges_from(mst_edges)
    nx.draw_networkx_edges(mst_g, pos, width=2, edge_color='blue')
    
    # Labels
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='orange')
    nx.draw_networkx_labels(G, pos)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.title(title)
    plt.savefig("mst_viz.png")
    print("MST visualization saved to mst_viz.png")