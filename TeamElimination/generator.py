import random   
import numpy as np
import math
import time


max_int = 1000000000
def ncr(a,b):
    return math.factorial(a)/(math.factorial(a-b) * math.factorial(b))

random.seed()
num_of_teams = int(input("Enter the number of teams: "))
num_of_games_to_play = random.randint(5,10)
play_counts = np.zeros((num_of_teams,num_of_teams)) 
games_to_play = np.ones((num_of_teams,num_of_teams)) * num_of_games_to_play
stats = np.zeros((num_of_teams,3))
start = time.time()
with open("baseball_"+str(num_of_teams)+".txt","w") as f:
    f.write(str(num_of_teams))
    f.write("\n")
    for i in range(num_of_teams):
        for j in range(i+1,num_of_teams):        
            val = random.randint(0,num_of_games_to_play)
            play_counts[i][j] = val
            play_counts[j][i] = play_counts[i][j]
            win_lose = np.random.randint(2,size=val)
            for k in win_lose:
                if k:
                    stats[i][0] += 1
                    stats[j][1] += 1
                else:
                    stats[i][1] += 1
                    stats[j][0] += 1
    left_to_play = games_to_play - play_counts
    for i in range(num_of_teams):
        left_to_play[i][i] = 0
        stats[i][2] = left_to_play[i].sum()  

    for row in stats.astype(int):
        for i in range(len(row)):
            f.write(str(row[i]))
            if len(row) - i == 1:
                f.write("\n")
            else:
                f.write(" ")

    for row in left_to_play.astype(int):
        for i in range(len(row)):
            f.write(str(row[i]))
            if len(row) - i == 1:
                f.write("\n")
            else:
                f.write(" ")
end = time.time()
duration = end - start
print(f"Baseball Stat File {i+1} created in {duration}s")


def generate_graph(stats, left_to_play, team):
    start = time.time()
    num_of_teams = len(left_to_play)
    layer1 = int(ncr(num_of_teams - 1,2))
    number_of_vertices =  layer1 + (num_of_teams - 1) + 2
    number_of_edges = layer1 * 3 + (num_of_teams - 1)
    offset = layer1 + 2
    edgelist = []
    vertex_counter = 2
    level1counter = 0
    limit = 0
    for i in range(num_of_teams):
        if i==team-1:
            continue
        level2counter = level1counter + 1
        for j in range(i+1,num_of_teams):
            if j != team-1:
                capacity = int(left_to_play[i][j])
                limit += capacity
                edgelist.append([1 ,vertex_counter ,capacity])
                edgelist.append([vertex_counter ,level1counter + offset ,max_int])
                edgelist.append([vertex_counter ,level2counter + offset ,max_int])
                vertex_counter += 1
                level2counter += 1
        level1counter += 1
    level1counter = 0
    for i in range(num_of_teams):
        if i != team-1:
            capacity = int(stats[team-1][0] + stats[team-1][2] - stats[i][0])
            edgelist.append([offset + level1counter ,number_of_vertices ,capacity])
            level1counter += 1

    with open ("graph_"+str(num_of_teams)+"_"+str(team)+".txt","w") as g:
        g.write(str(number_of_vertices) + " " + str(number_of_vertices) + " " + str(number_of_edges)+"\n")
        for row in edgelist:
            for i in range(len(row)):
                g.write(str(row[i]))
                if len(row) - i == 1:
                    g.write("\n")
                else:
                    g.write(" ")
    with open("stats.txt","a") as f:
        f.write(str(limit)+"\n")
    duration = time.time() - start
    print(f"Graph file No {team} created in {duration}s")

for i in range(num_of_teams):
    generate_graph(stats,left_to_play,i+1)
