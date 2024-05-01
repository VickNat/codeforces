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
  N = InputInt()
  t = InputStr()
  v = InputStr()
  parent = {i : i for i in range(97, 123)}
  size = {i : 1 for i in range(97, 123)}
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
    
  for i in range(N):
    union(ord(t[i]), ord(v[i]))
  
  for i in range(97, 123):
    val = chr(find(i))
    if val != chr(i):
      ans.append([val, chr(i)])
  
  print(len(ans))
  for a, b in ans:
    print(a, b)

main()