import osmnx as ox

print("Loading Waterloo road network...")

graph = ox.io.load_graphml(filepath='data/raw/waterloo_drive.graphml')

print("Load complete.")
print(f"Nodes: {len(graph.nodes)}")
print(f"Edges: {len(graph.edges)}")

# show one real road-nework node and one real rode segment including the info attached to them
node_id, node_data = next(iter(graph.nodes(data=True)))

print("\nExample node:")
print("ID:", node_id)
print("Data:", node_data)

u, v, edge_data = next(iter(graph.edges(data=True)))

print("\nExample edge:")
print("From:", u)
print("To:", v)
print("Data:", edge_data)