from matplotlib import pyplot as plt, animation
import networkx as nx
import random

from networkx.algorithms.bipartite.basic import color

plt.rcParams["figure.figsize"] = [10.0, 10.0]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

G = nx.Graph()
graph_size = 20
for i in range(0, graph_size):
    G.add_node(i)
for i in range(0, graph_size):
    for j in range (i+1, graph_size):
        G.add_edge(i, j)
G.add_edge(graph_size-1, 0)

nx.draw_kamada_kawai(G, node_color="cornflowerblue", with_labels=False)

def animate(frame):
    fig.clear()
    color_map = [] 
    for node in G:
        fire = bool(random.getrandbits(1))
        if fire:
            color_map.append("yellow")
        else:
            color_map.append("cornflowerblue")
    
    nx.draw_kamada_kawai(G, node_color=color_map, with_labels=False)

ani = animation.FuncAnimation(fig, animate, frames=1000, interval=100, repeat=True)

plt.show()