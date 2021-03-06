from matplotlib import pyplot as plt, animation
import networkx as nx
import random
import numpy as np
import Model_for_nx as mnx

N = 50
end_time = 20
dt = 1E-2
result = mnx.run_simulation(N=N, end_time=end_time, dt=dt) 

plt.rcParams["figure.figsize"] = [8.0, 6.0]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
G = nx.DiGraph()
for i in range(0, N):
    G.add_node(i)

pos = nx.random_layout(G, seed=42)

nx.draw(G, pos=pos, node_color='cornflowerblue', node_size=100)

def animate(frame):
    timestep=frame * end_time
    fig.clear()
    color_map_node = [] 
    color_map_edge = []
    for node in G:
        fire = result.spike_record[node][timestep]
        # print("Node: " + str(node) + "\t Frame: " + str(timestep) + "\tFire: " + str(fire))
        if fire > 0.9:
            color_map_node.append("pink")
            color_map_edge.append("pink")
        else:
            color_map_node.append("cornflowerblue")
            color_map_edge.append("black")


    nx.draw(G, pos=pos, node_color=color_map_node, node_size=100)

frames = int(len(result.time_record[0]) / end_time)
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=100, repeat=True)
writergif = animation.PillowWriter(fps=10)
ani.save('./ani.gif', writer=writergif)
plt.show()

