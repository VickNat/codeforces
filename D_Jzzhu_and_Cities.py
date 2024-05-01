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

def dijkstra(graph, trains):
  start = 1
  distances = [float('inf') for _ in range(len(graph))]
  distances[start] = 0
  visited = set()
  importantTrains = 0

  priorityQueue = [(0, start, False)]

  for v, w in trains:
    heapq.heappush(priorityQueue, (w, v, True))

  print(priorityQueue)

#   while priorityQueue:
#     curWeight, curNode, isTrain = heapq.heappop(priorityQueue)

#     if isTrain:
#       if distances[curNode] <= curWeight:
#         importantTrains += 1
#         continue
#       elif distances[curNode] > curWeight:
#         distances[curNode] = curWeight

#     if curNode in visited:
#       continue
    
#     visited.add(curNode)

#     for neighbour, weight in graph[curNode]:
#       distance = curWeight+weight
#       if distance < distances[neighbour]:
#         distances[neighbour] = distance
#         heapq.heappush(priorityQueue, (distance, neighbour))

#   return importantTrains

# def main():
#   N, M, K = InputList()
#   graph = [[] for i in range(N+1)]
#   trains = []

#   for _ in range(M):
#     u, v, w = InputList()
#     graph[u].append((v, w))
#     graph[v].append((u, w))
  
#   for _ in range(K):
#     u = 1
#     v, w = InputList()
#     trains.append((v, w))
  
#   importantTrains = dijkstra(graph, trains)
#   print(importantTrains)


# T = 1
# for _ in range(T):
#   main()


# import sys
# from collections import defaultdict , deque 
# from heapq import heappush , heappop
# n , m , k = map(int , sys.stdin.readline().split())
# parent = defaultdict(int)

# visited = [False]*(10**5 + 1)
# distances =[float('inf')]*(10**5 + 1)
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     start , end , width = map(int , sys.stdin.readline().split())
    
#     graph[start].append((end , width))
#     graph[end].append((start , width))


# ans = 0
# distances[1] = 0
# heap = [( 0 , 1 , False)]

# for _ in range(k):
    
#     end , width = map(int , sys.stdin.readline().split())
#     heappush(heap , (width , end , True))

# while heap:
#     distance , node , t = heappop(heap)

#     if distances[node] <= distance and t: 
#         ans += 1
#         continue
#     elif distances[node] > distance and t:
#         distances[node] = distance

#     if visited[node]:
#         continue
#     visited[node] = True

#     for child , width in graph[node]:
#         if distance + width < distances[child]:
#             distances[child] = distance + width
#             heappush( heap , (distances[child] , child , False))

    
# print(ans )