#import libraties
import networkx as nx
import matplotlib.pyplot as plt

#creating the graph
DG = nx.DiGraph()
#adding nodes
node = ["Happy", "Theresa", "Esther", "Gidi", "Okai", "Tagoe", "Bingo"]
# Adding Edges
edges = [("Happy", "Bingo"),("Happy", "Tagoe"),("Esther", "Tagoe") ,("Esther", "Theresa"),("Happy", "Gidi"), ("Okai", "Tagoe"),("Okai", "Bingo"), ("Happy", "Theresa")]
DG.add_edges_from(edges)
#Customising the graph
draw = nx.draw(DG, with_labels=True, node_size=1600, font_size=10, font_color="yellow", arrows=False)
plt.show()
#Outputting the number of Edges and Nodes
print(f"Graph created with {DG.number_of_nodes()} nodes and {DG.number_of_edges()} edges.")
#Finding the degree Distribution for each individual node in the graph
degrees = [DG.degree(node) for node in DG.nodes()]
print("Degree distribution:")
for node, degree in DG.degree():
    print(f"  {node}: {degree}")
#Locating isolated nodes if any
isolated_nodes = [node for node, degree in DG.degree() if degree == 0]
if isolated_nodes:
    print(f"\nIsolated nodes: {isolated_nodes}")
else:
    print("\nNo isolated nodes found.")
#Visualization using mathplot
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
nx.draw_networkx(DG, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray', font_size=10, font_weight='bold', arrows=False)
plt.title('My Research Group Network Visualization ')
plt.axis('off')
plt.show()

degree_sequence = sorted([d for n, d in DG.degree()], reverse=True)
degree_counts = nx.degree_histogram(DG)

plt.figure(figsize=(8, 6))
plt.bar(range(len(degree_counts)), degree_counts, width=0.8, color='orange')
plt.title('Degree Distribution')
plt.xlabel('Degree')
plt.ylabel('Number of Nodes')
plt.xticks(range(len(degree_counts)))
plt.show()

