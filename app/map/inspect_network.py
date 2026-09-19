import osmnx as ox

print("Loading Waterloo road network...")

graph = ox.io.load_graphml(filepath='data/raw/waterloo_drive.graphml')

print("Load complete.")
print(f"Nodes: {len(graph.nodes)}")
print(f"Edges: {len(graph.edges)}")

# show one real road-network node and one real rode segment including the info attached to them
node_id, node_data = next(iter(graph.nodes(data=True)))

print("\nExample node:")
print("ID:", node_id)
print("Data:", node_data)

u, v, edge_data = next(iter(graph.edges(data=True)))

print("\nExample edge:")
print("From:", u)
print("To:", v)
print("Data:", edge_data)

print("\nPlotting road network...")

fig, ax = ox.plot_graph(
    graph,
    node_size = 0,
    edge_linewidth = 0.8,
    show = False,
    close = False
)

fig.savefig(
    "data/raw/waterloo_road_network.png",
    dpi = 200,
    bbox_inches = 'tight'
)

print("Map image saved.")
