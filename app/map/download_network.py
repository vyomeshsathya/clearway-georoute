import osmnx as ox

print("Downloading Waterloo road network...")

graph = ox.graph.graph_from_place('Waterloo, Ontario, Canada', network_type='drive')

print("Download complete. ")
print(f"Nodes: {len(graph.nodes)}")
print(f"Edges: {len(graph.edges)}")

ox.io.save_graphml(graph, filepath='data/raw/waterloo_drive.graphml')

print("Road network saved.")