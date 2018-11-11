# Represents a graph that maintains an adjacency list
class Graph
  def initialize
    @graph = {}
  end

  def add_edge(vertex, adjacent_vertex)
    (@graph[vertex] ||= []).push(adjacent_vertex)
  end

  def dfs_iterative(start)
    stack = [start]
    visited = []
    until stack.empty?
      vertex = stack.pop
      continue if visited.include?(vertex)
      visited.push(vertex)
      @graph[vertex].each do |adjacent_vertex|
        stack.push(adjacent_vertex) unless visited.include?(adjacent_vertex)
      end
    end
    visited
  end

  def dfs_recursive(start, visited = nil)
    visited ||= []
    visited.push(start)
    @graph[start].each do |adjacent_vertex|
      unless visited.include?(adjacent_vertex)
        visited = dfs_recursive(adjacent_vertex, visited)
      end
    end
    visited
  end

  def breadth_first_traversal(start)
    queue = [start]
    visited = []
    until queue.empty?
      vertex = queue.delete_at(0)
      visited.push(vertex)
      @graph[vertex].each do |adjacent_vertex|
        queue.push(adjacent_vertex) unless visited.include?(adjacent_vertex)
      end
    end
    visited
  end
end

graph = Graph.new
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print graph.dfs_iterative(2)
print graph.dfs_recursive(2)
print graph.breadth_first_traversal(2)
