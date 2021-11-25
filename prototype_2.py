from matplotlib import pyplot as plt, animation
import networkx as nx
import random
import numpy as np
import Model_for_nx as mnx

result = mnx.run_simulation(N=500,end_time=20, dt=1) 

plt.rcParams["figure.figsize"] = [10.0, 10.0]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
graph_size = len(result)
G = nx.DiGraph()
for i in range(0, graph_size):
    G.add_node(i)
    
#FOR 4 OUTGOING EDGES PER NODE
#for i in range(0, graph_size):
#    for j in range(i+1, i+5):
#        G.add_edge(i, j)

pos = nx.random_layout(G, seed=42)

nx.draw(G, pos=pos, node_color='cornflowerblue', node_size=100)

def animate(frame):
    timestep=frame
    fig.clear()
    color_map_node = [] 
    color_map_edge = []
    for node in G:
        neuron = result[node-1]
        fire = bool(neuron[timestep])
        if fire:
            color_map_node.append("yellow")
            color_map_edge.append("yellow")
        else:
            color_map_node.append("cornflowerblue")
            color_map_edge.append("black")


    nx.draw(G, pos=pos, node_color=color_map_node, node_size=100)

#edge_color=color_map_edge

ani = animation.FuncAnimation(fig, animate, frames=20, interval=20, repeat=True)

plt.show()

