def bellman_ford(n, edges, src):

    prev = [float('inf')] * n
    prev[src] = 0
    
    # Perform N-1 iterations (where N is the number of nodes)
    
    for i in range(n-1):
        curr = prev[:]
        # Relax all edges    
        for u, v, w in edges:
            curr[v] = min(curr[v], prev[u]+w)
            # Swap the arrays, prev now points to curr
            prev = curr[:]
    
    return prev
