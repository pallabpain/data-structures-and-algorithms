#!/usr/bin/env python
# pylint:disable=invalid-name

"""
This file contains implementation of a graph as an adjacency list
and the breadth-first and depth-first traversals on it.
"""

from __future__ import print_function

from collections import defaultdict


class Graph(object):
    """
    Represents a graph that maintains an adjacency list
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, adjacent_vertex):
        """
        Adds a new edge to the graph
        """
        self.graph[vertex].append(adjacent_vertex)

    def dfs_iterative(self, start):
        """
        Iterative implementation of the depth first traversal
        """
        stack, path = [start], []
        while stack:
            vertex = stack.pop()
            if vertex in path:
                continue
            path.append(vertex)
            for adjacent_vertex in self.graph[vertex]:
                stack.append(adjacent_vertex)
        return path

    def dfs_recursive(self, start, visited=None):
        """
        Recursive implementation of the depth-first traversal
        """
        visited = visited or []
        visited += [start]
        for adjacent_vertex in self.graph[start]:
            if adjacent_vertex not in visited:
                visited = self.dfs_recursive(adjacent_vertex, visited)
        return visited

    def breath_first_traversal(self, start):
        """
        Return the breadth-first traversal path
        """
        queue, visited = [start], []
        while queue:
            vertex = queue.pop(0)
            visited.append(vertex)
            for adjacent_vertex in self.graph[vertex]:
                if adjacent_vertex not in visited:
                    queue.append(adjacent_vertex)
        return visited


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print(graph.dfs_recursive(2))
    print(graph.dfs_iterative(2))
    print(graph.breath_first_traversal(2))
