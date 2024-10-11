def spfa(n, graph, src):
    # Initialize distance, in_queue, and count arrays
    dist = [float('inf')] * n
    in_queue = [False] * n
    count = [0] * n
    # Tracks number of edges in the current shortest path for each vertex
    dist[src] = 0
    # Queue to store nodes to process
    queue = deque([src])
    in_queue[src] = True

    while queue:
        u = queue.popleft()
        in_queue[u] = False
        for v, w in graph[u]:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                count[v] = count[u] + 1

            if count[v] >= n:
                print("Negative cycle exits")
                return None

            if not in_queue[v]:
                queue.append(v)
                in_queue[v] = True
    return dist
