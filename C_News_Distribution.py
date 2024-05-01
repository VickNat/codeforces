import math
from collections import defaultdict
from collections import Counter
from collections import deque
import heapq

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))
def InpStrToList(): return list(input())

def main():
  n, m = InputIterables()
  parent = {i : i for i in range(1, n+1)}
  size = {i : 1 for i in range(1, n+1)}
  ans = []
          
  def find(x):
    root = x

    while root != parent[root]:
      root = parent[root]
    
    while x != parent[x]:
      temp = parent[x]
      parent[x] = root
      x = temp

    return root

  def union(x, y):
    x_rep = find(x)
    y_rep = find(y)

    if x_rep != y_rep:
      if size[x_rep] < size[y_rep]:
        x_rep, y_rep = y_rep, x_rep
      
      size[x_rep] += size[y_rep]
      parent[y_rep] = parent[x_rep]
    
  for _ in range(m):
    k, *group = InputList()
    prev = -1

    for elm in group:
      if prev != -1:
        union(elm, prev)
      prev = elm
  
  for i in range(1, n+1):
    ans.append(size[find(i)])

  print(*ans)

main()