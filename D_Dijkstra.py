import math
from collections import defaultdict
from collections import Counter
from collections import deque
import heapq

def InputStr(): return input()
def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))
def InputRevSortedList(): return list(reversed(sorted(list(map(int, input().split())))))
def InpStrToList(): return list(input())


def dijkstra(graph, start, end):
  distances = {node: float('inf') for node, val in graph.items()}
  relaxants = {node: float('inf') for node, val in graph.items()}
  distances[start] = 0
  relaxants[start] = None
  visited = set()


  priorityQueue = [(0, start)]

  while priorityQueue:
    curWeight, curNode = heapq.heappop(priorityQueue)

    if curNode in visited:
      continue
    
    visited.add(curNode)

    for neighbour, weight in graph[curNode]:
      distance = curWeight+weight
      if distance < distances[neighbour]:
        distances[neighbour] = distance
        heapq.heappush(priorityQueue, (distance, neighbour))
        relaxants[neighbour] = curNode
  
  if distances[end] == float('inf'):
    return -1

  parents = end
  ans = []
  while parents != None:
    ans.append(parents)
    parents = relaxants[parents]

  return ans

def main():
  N, M = InputList()
  graph = {i: [] for i in range(1, N+1)}
  
  for _ in range(M):
    a, b, w = InputList()
    graph[a].append((b, w))
    graph[b].append((a, w))

  ans = dijkstra(graph, 1, N)
  if ans == -1:
    print(ans)
  else:
    print(*(reversed(ans)))
  

T = 1
for _ in range(T):
  main()