def dfs(idx):
    for edge in edges[idx]:
      if visited[edge-1] == visited[idx]:
        return False
      
      if visited[edge-1] == 0:
        visited[edge-1] = 3-visited[idx]
      
        if not dfs(edge-1):
          return False
      
    return True