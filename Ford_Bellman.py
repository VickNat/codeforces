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

def main():
  N, M = InputList()
  graph = []
  distances = [float('inf') for i in range(N)]
  distances[0] = 0

  for _ in range(M):
    a, b, w = InputList()
    graph.append((a-1, b-1, w))
  
  for i in range(N-1):
    for i, j, w in graph:
      newWeight = w + distances[i]
      if distances[i] != float('inf') and newWeight < distances[j]:
        distances[j] = newWeight
  
  distances = [num if num != float('inf') else 30000 for num in distances]
  print(*distances)

T = 1
for _ in range(T):
  main()