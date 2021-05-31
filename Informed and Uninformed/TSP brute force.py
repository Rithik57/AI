from itertools import permutations
from sys import maxsize

V = 4

def TSP(graph, S): #receives the graph and the starting vertex
    # store all non active vertices in a list
    vertex = []
    for i in range(V):  # V -> number of vertices
        if i != S:
            vertex.append(i)
    minPath = maxsize
    # consider all permutations
    current = permutations(vertex)
    for x in current:
        currentWeight = 0
        # for the current permutation add all paths
        begin = S
        for end in x:
            currentWeight = currentWeight + graph[begin][end]
            begin = end
        currentWeight = currentWeight + graph[end][S] # add weight from last vertex to start to complete cycle
        # check if the min path was found in this permutation
        minPath = min(minPath, currentWeight)
        print("weight for permutation : " + str(x) + " is : " + str(currentWeight))
    return minPath


graph1 = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
start = int(input("Enter the starting vertex : "))
print("the min path weight for the graph is : "+str(TSP(graph1,start)))