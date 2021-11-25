from matplotlib import pyplot as plt, animation
import networkx as nx
import random

from networkx.algorithms.bipartite.basic import color

plt.rcParams["figure.figsize"] = [5.0, 5.0]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4])
for i in range(0, 10):
    G.add_node(i)
for i in range(0, 9):
    G.add_edge(i, i+1)
G.add_edge(9, 0)

nx.draw(G, node_color="cornflowerblue", with_labels=True)

def animate(frame):
    fig.clear()
    color_map = [] 
    for node in G:
        fire = bool(random.getrandbits(1))
        if fire:
            color_map.append("yellow")
        else:
            color_map.append("cornflowerblue")
    
    nx.draw_circular(G, node_color=color_map, with_labels=True)

ani = animation.FuncAnimation(fig, animate, frames=20, interval=250, repeat=True)

plt.show()