"""
Dijkstra.py
@author: Yusan
@date: 2014/08/11
@description: implementationg of Dijkstra algorithm,
               finding the shortest paths in a given network graph
"""
import numpy as np

VERY_BIG_NUMBER = 1000000
INF = float("inf")

def Dijkstra(Graph, source):
    n_nodes = len(Graph)
    dist = [0]*n_nodes
    previous = [0]*n_nodes
    Q = []
    
    dist[source] = 0

    for v in range(n_nodes):
        if v != source:
            dist[v] = INF
            previous[v] = float("nan")
        Q.append(v)

    finish = False
    while len(Q) != 0 and not(finish):
        u = MinDist(Q, dist, source)
        if u < n_nodes:
            Q.remove(u)
            for v in Neighbors(Graph, u):
                alt = dist[u] + Graph[u][v]
    
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u
        else:
            finish = True
            
    return dist, previous

def Neighbors(Graph, u):
    n = len(Graph)
    u_row = Graph[u]
    u_neighbors = []

    for i in range(len(u_row)):
        if u_row[i] != INF and u_row[i] != 0:
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
    
    while not found and i < len(dist):
        i += 1
        
        if np.where(dist_copy == dist_copy.min())[0][0] == i\
           and i in Q:
            found = True
        else:
            try:
                dist_copy[i] = VERY_BIG_NUMBER
            except IndexError:
                break
    

    return i

# Sample networks for testing
graph1 = [[  0,  2,  8,  5,INF],\
         [INF,  0,  1,INF,INF],\
         [INF,INF,  0,INF,  3],\
         [INF,INF,INF,  0,  4],\
         [INF,INF,INF,INF,  0]]

graph2 = [[  0,  1,INF,INF],\
          [INF,  0,  3,INF],\
          [INF,INF,  0,  2],\
          [INF,INF,INF,  0]]