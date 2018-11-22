#!/usr/bin/env python
"""
This file contains the implementation of Prim's algorithm for minimum
cost spanning tree in a connected and weighted graph using adjacency
matrix. The time complexity using adjacency matrix in this implmentation
comes out to O(n^2).
"""

from __future__ import print_function

INF = float("inf")


class Graph(object):

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def _print_mst(self, parent):
        print("Edge\tWeight")
        for v in range(1, self.vertices):
            print("{}-{}\t{}".format(parent[v], v, self.graph[v][parent[v]]))

    def _find_min_weight_edge(self, weight, visited):
        """
        Finds the vertex with the minimum edge cost from the set
        of vertices that not yet visited
        """
        minimum = INF
        min_index = None
        for v in range(self.vertices):
            if weight[v] < minimum and not visited[v]:
                minimum = weight[v]
                min_index = v
        return min_index

    def prims_minimum_spanning_tree(self):
        weight = [INF] * self.vertices
        parent = [None] * self.vertices
        visited = [False] * self.vertices
        # Picking 0 as the first vertex. Its weight will be 0
        weight[0] = 0
        # First node is the root, so parent will be -1
        parent[0] = -1

        for _ in range(self.vertices):
            u = self._find_min_weight_edge(weight, visited)
            visited[u] = True
            for v in range(self.vertices):
                if u == v:
                    continue
                if self.graph[u][v] and not visited[v] and weight[v] > self.graph[u][v]:
                    weight[v] = self.graph[u][v]
                    parent[v] = u
        self._print_mst(parent)


if __name__ == "__main__":
    graph = Graph(5)
    graph.graph = [[0, 2, 0, 6, 0],
                   [2, 0, 3, 8, 5],
                   [0, 3, 0, 0, 7],
                   [6, 8, 0, 0, 9],
                   [0, 5, 7, 9, 0]]
    graph.prims_minimum_spanning_tree()
