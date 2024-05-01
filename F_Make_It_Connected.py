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
def InpStrToList(): return list(input())

def main():
  N, M = InputIterables()
  arr = InputList()
  parent = {i : i for i in range(1, N+1)}
  size = {i : 1 for i in range(1, N+1)}
  edges = []
  minIdx = 0
  minVal = float('inf')
  ans = 0

  for _ in range(M):
      x, y, w = InputIterables()
      edges.append((w, x, y))

  for idx, val in enumerate(arr):
    if val < minVal:
      minVal = val
      minIdx = idx
  
  for idx, val in enumerate(arr):
    if minIdx != idx:
      w = val + minVal
      edges.append((w, minIdx+1, idx+1))
  
  edges.sort()

  def find(x):
    root = x

    while root != parent[root]:
      root = parent[root]
    
    while x != parent[x]:
      x, parent[x] = parent[x], root

    return root

  def union(x, y):
    x_rep = find(x)
    y_rep = find(y)

    if x_rep != y_rep:
      if size[x_rep] < size[y_rep]:
        x_rep, y_rep = y_rep, x_rep
      
      size[x_rep] += size[y_rep]
      parent[y_rep] = parent[x_rep]

  for w, x, y in edges:
    if find(x) != find(y):
      ans += w
    union(x, y)
  
  print(ans)
    


main()