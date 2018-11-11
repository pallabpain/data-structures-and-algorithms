# Finds the unvisited vertex with the minimum weight
def min_distance_vertex(distance, visited)
  vertices = visited.length
  min_distance = Float::INFINITY
  min_index = nil
  0.upto(vertices - 1) do |v|
    if !visited[v] && distance[v] <= min_distance
      min_distance = distance[v]
      min_index = v
    end
  end
  min_index
end

def dijkstra(graph, source)
  vertices = graph.length
  visited = [false] * vertices
  distance = [Float::INFINITY] * vertices
  distance[source] = 0
  1.upto(vertices - 1) do
    u = min_distance_vertex(distance, visited)
    visited[u] = true
    0.upto(vertices - 1) do |v|
      next unless !visited[v] && graph[u][v] != 0 &&
                  distance[u] != Float::INFINITY &&
                  distance[u] + graph[u][v] < distance[v]

      distance[v] = distance[u] + graph[u][v]
    end
  end
  puts "Vertex\tDistance from source"
  distance.each_with_index do |d, i|
    puts format("%-6d\t%d", i, d)
  end
end

graph = [
  [0, 4, 0, 0, 0, 0, 0, 8, 0],
  [4, 0, 8, 0, 0, 0, 0, 11, 0],
  [0, 8, 0, 7, 0, 4, 0, 0, 2],
  [0, 0, 7, 0, 9, 14, 0, 0, 0],
  [0, 0, 0, 9, 0, 10, 0, 0, 0],
  [0, 0, 4, 14, 10, 0, 2, 0, 0],
  [0, 0, 0, 0, 0, 2, 0, 1, 6],
  [8, 11, 0, 0, 0, 0, 1, 0, 7],
  [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

dijkstra(graph, 0)
