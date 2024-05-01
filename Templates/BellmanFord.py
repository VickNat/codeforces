class Graph:
  def __init__(self, numberOfVertices):
    self.V = numberOfVertices
    self.graph = []
    def add_edge(self, u, v, w):
      self.graph.append([u, v, w])

def bellman_ford(self, src):
  dist = [float("inf")] * numOfVertices
  dist[src] = 0
  for _ in range(numOfVertices - 1):
    for u, v, w in self.graph:
      if dist[u] != float("inf") and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w

  for u, v, w in self.graph:
    if dist[u] != float("inf") and dist[u] + w < dist[v]:
      print("Negative Cycle Detected")
      return 
      print(dist)