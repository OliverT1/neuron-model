from matplotlib import pyplot as plt, animation
import networkx as nx
import random
import numpy as np

plt.rcParams["figure.figsize"] = [10.0, 10.0]
plt.rcParams["figure.autolayout"] = True




fig = plt.figure()
graph_size = 50
G = nx.DiGraph()
for i in range(0, graph_size):
    G.add_node(i)

for i in range(0, graph_size):
    for j in range(i+1, i+5):
        G.add_edge(i, j)

pos = nx.random_layout(G, seed=42)

nx.draw(G, pos=pos, node_color='cornflowerblue', node_size=100)

def animate(frame):
    fig.clear()
    color_map_node = [] 
    color_map_edge = []
    for node in G:
        fire = bool(random.getrandbits(1))
        if fire:
            color_map_node.append("yellow")
            color_map_edge.append("yellow")
        else:
            color_map_node.append("cornflowerblue")
            color_map_edge.append("black")

    nx.draw(G, pos=pos, node_color=color_map_node, edge_color=color_map_edge, node_size=100)

ani = animation.FuncAnimation(fig, animate, frames=1000, interval=500, repeat=True)

plt.show()

