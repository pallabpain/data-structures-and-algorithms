
INF = float("inf")


def min_distance_vertex(distance, visited):
    """
    Returns the index of the vertex that is not visited
    and has the minimum distance value
    """
    vertices = len(visited)
    min_distance = INF
    min_index = None
    for v in range(vertices):
        if not visited[v] and distance[v] <= min_distance:
            min_distance = distance[v]
            min_index = v
    return min_index


def djikstra(graph, source):
    vertices = len(graph)
    distance = [INF] * vertices
    visited = [False] * vertices

    # Distance from source to itself will be 0
    distance[source] = 0

    for _ in range(vertices - 1):
        # Pick the minimum distance vertex that is unvisited
        u = min_distance_vertex(distance, visited)
        # Mark the vertex as visited
        visited[u] = True
        # For each vertex v, update distance[v] if,
        # 1. It is not visited
        # 2. There is an edge from u to v
        # 3. Total weight of the path from source to v through u
        #    is smaller than the current weight i.e. distance[v]
        for v in range(vertices):
            if (not visited[v] and graph[u][v] and distance[u] != INF
                    and distance[u] + graph[u][v] < distance[v]):
                distance[v] = distance[u] + graph[u][v]

    print("Vertex\tDistance")
    for i, d in enumerate(distance):
        print("{}\t{}".format(i, d))


# Driver code
if __name__ == "__main__":
    # Adjacendy matrix
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
    djikstra(graph, 0)
