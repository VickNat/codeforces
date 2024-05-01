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
  N = InputInt()+1
  edges = InputList()
  colors = InputList()
  graph = [[] for i in range(N)]

  queue = deque()
  visited = set()

  for i, val in enumerate(edges):
    graph[val].append(i+2)
  
  counts = 1
  queue.append(1)
  visited = set()
  visited.add(1)

  while queue:
    cur = queue.popleft()

    for node in graph[cur]:
      if node not in visited:
        if colors[cur-1] != colors[node-1]:
          counts += 1
        queue.append(node)
        visited.add(node)
      
  print(counts)

main()