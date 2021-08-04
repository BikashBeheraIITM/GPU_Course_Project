import numpy as np
import random
def generate_nodes(supply_nodes, num ,nodes):
    out = set()
    while(len(out) < num):
        val = random.randint(2,nodes-1)
        if val not in supply_nodes:
            out.add(val)
    return out
for k in range(50):
    with open("temp.mtx","r") as f:
        with open("graph_"+str(k)+".txt","w") as g:
            line = f.readline()
            values = line.strip("\n").split(" ")
            org_edges = int(values[2])
            nodes = int(values[0]) + 2
            s_nodes = int(nodes/1000)
            d_nodes = int(nodes/1000)
            supply_nodes = set()
            demand_nodes = set()
            supply_nodes = generate_nodes(supply_nodes,s_nodes,nodes)
            demand_nodes = generate_nodes(supply_nodes,d_nodes,nodes)
            source_node = 1
            sink_node = nodes
            edges = int(values[2]) + s_nodes + d_nodes
            val = int(values[2]) + s_nodes + d_nodes
            g.write(str(nodes) + " " + str(nodes) + " " + str(val) + "\n")
            for i in range(org_edges):
                line = f.readline().strip("\n")
                temp = line.split(" ")
                v1 = int(temp[0]) + 1
                v2 = int(temp[1]) + 1
                towrite = str(v1) + " " + str(v2) + " 1\n" 
                g.write(towrite)

    total_supply = 0
    total_demand = 0  

    supply_edges = np.zeros((s_nodes,3))    
    demand_edges = np.zeros((d_nodes,3))
    with open("graph_"+str(k)+".txt", "a") as f:
        i = 0
        for val in supply_nodes:
            supply_edges[i][0] = source_node
            supply_edges[i][1] = val
            supply_edges[i][2] = np.random.randint(1,7)
            total_supply += supply_edges[i][2]
            f.write(str(int(supply_edges[i][0])) + " "+ str(int(supply_edges[i][1])) + " "+  str(int(supply_edges[i][2])) + "\n")
            i += 1
        i = 0
        for val in demand_nodes:
            demand_edges[i][0] = val
            demand_edges[i][1] = sink_node
            demand_edges[i][2] = np.random.randint(1,4)
            total_demand += demand_edges[i][2]
            f.write(str(int(demand_edges[i][0])) + " "+ str(int(demand_edges[i][1])) + " "+  str(int(demand_edges[i][2])) + "\n")
            i += 1



    with open("stats_"+str(k)+".txt",'w') as f:
        f.write(str(total_supply) + " " + str(total_demand) + "\n")

    
