def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    processed = set()
    heap = [(0, start_node)]
    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_node in processed:
            continue
        processed.add(current_node)
        for child, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[child]:
                distances[child] = distance
                heapq.heappush(heap, (distance, child))
    return distances
