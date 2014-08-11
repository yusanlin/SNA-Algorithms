"""
Dijkstra.py
@author: Yusan
@date: 2014/08/11
@description: implementationg of Dijkstra algorithm,
               finding the shortest paths in a given network graph
"""
import numpy as np

VERY_BIG_NUMBER = 1000000

def Dijkstra(Graph, source):
    n_nodes = len(Graph)
    dist = [0]*n_nodes
    previous = [0]*n_nodes
    Q = []
    
    dist[source] = 0

    for v in range(n_nodes):
        if v != source:
            dist[v] = float("inf")
            previous[v] = float("nan")
        Q.append(v)

    while len(Q) != 0:
        u = MinDist(Q, dist, source)
        Q.remove(u)
        for v in Neighbors(Graph, u):
            alt = dist[u] + Graph[u][v]

            if alt < dist[v]:
                dist[v] = alt
                previous[v] = u
            
    return dist, previous

def Neighbors(Graph, u):
    n = len(Graph)
    u_row = graph[u]
    u_neighbors = []

    for i in range(len(u_row)):
        if u_row[i] != float("inf") and u_row[i] != 0:
            u_neighbors.append(i)

    return u_neighbors

def MinDist(Q, dist, source):
    min_dist = VERY_BIG_NUMBER
    i = -1

    found = False
    
    dist_copy = []
    for d in dist:
        dist_copy.append(d)
    dist_copy = np.array(dist_copy)
    
    while not found:
        i += 1
        
        if np.where(dist_copy == dist_copy.min())[0][0] == i\
           and i in Q:
            found = True
        else:
            dist_copy[i] = VERY_BIG_NUMBER
        
    return i

graph = [[0,2,8,5,float("inf")],\
         [float("inf"),0,1,float("inf"),float("inf")],\
         [float("inf"),float("inf"),0,float("inf"),3],\
         [float("inf"),float("inf"),float("inf"),0,4],\
         [float("inf"),float("inf"),float("inf"),float("inf"),0]]
