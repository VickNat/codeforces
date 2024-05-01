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
  N, D = InputIterables()
  parent = {i : i for i in range(1, N+1)}
  size = {i : 1 for i in range(1, N+1)}
  free_edges = 1

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
      size[y_rep] = 1
      parent[y_rep] = parent[x_rep]
  
  def maxCounter():
    max_ = 0
    sortedArr = []

    for val in size.values():
      sortedArr.append(val)
    
    sortedArr.sort(reverse=True)

    for i in range(free_edges):
      max_ += sortedArr[i]
    
    return max_
    
  for _ in range(D):
    a, b = InputIterables()

    if find(a) != find(b):
      union(a, b)
    else:
      free_edges += 1
    
    print(maxCounter()-1)
    

main()