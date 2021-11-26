from matplotlib import pyplot as plt, animation
import networkx as nx
import random
import numpy as np
import Model_for_nx as mnx

N = 100
end_time = 5
dt = 1E-2
result = mnx.run_simulation(N=N, end_time=end_time, dt=dt) 

plt.rcParams["figure.figsize"] = [8.0, 8.0]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
G = nx.DiGraph()
for i in range(0, N):
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
        fire = result.time_record[node][timestep]
        # print("Node: " + str(node) + "\t Frame: " + str(timestep) + "\tFire: " + str(fire))
        if fire > 0.9:
            color_map_node.append("yellow")
            color_map_edge.append("yellow")
        else:
            color_map_node.append("cornflowerblue")
            color_map_edge.append("black")


    nx.draw(G, pos=pos, node_color=color_map_node, node_size=100)

#edge_color=color_map_edge
frames = len(result.time_record[0]) - 1
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=5, repeat=False)

plt.show()

