from functools import cache
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
  cats = InputList()
  graph = [[] for i in range(N)]
  visited = set()

  for _ in range(N-1):
    a, b = InputList()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
  
  visited.add(0)
  
  @cache
  def dp(node, catCounts):
    if catCounts > M:
      return 0
    if len(graph[node]) == 1 and node != 0:
      return 1
    
    counts = 0
    for child in graph[node]:
      if child not in visited:
        visited.add(child)
        if cats[child] == 1:
          counts += dp(child, catCounts+1)
        else:
          counts += dp(child, 0)

    return counts

  print(dp(0, cats[0]))

# T = InputInt()
T = 1
for _ in range(T):
  main()