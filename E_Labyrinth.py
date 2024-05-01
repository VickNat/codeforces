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
  rows, cols = InputList()
  rStart, cStart = InputList()
  left, right = InputList()
  graph = [[] for i in range(rows)]
  directions = [(1, 0), (-1, 0)]
  rStart -= 1
  cStart -= 1
  
  for i in range(rows):
    graph[i] = InpStrToList()
  
  def inbound(r, c):
    return 0 <= r < rows and 0 <= c < cols

  queue = deque()
  visited = [[(-1, -1) for c in range(cols)] for r in range(rows)]
  
  counts = 0
  queue.append((rStart, cStart, left, right))
  visited[rStart][cStart] = (left, right)

  while queue:
    r, c, l, rt = queue.popleft()

    for changeR, changeC in directions:
      newR = r+changeR
      newC = c+changeC

      if inbound(newR, newC) and graph[newR][newC] != "*":
        if visited[newR][newC] == (-1, -1):
          counts += 1
        if visited[newR][newC] < (l, rt):
          queue.append((newR, newC, l, rt))
          visited[newR][newC] = (l, rt)
    
    if l > 0:
      newR = r
      newC = c-1

      if inbound(newR, newC) and graph[newR][newC] != "*":
        if visited[newR][newC] == (-1, -1):
          counts += 1
        if visited[newR][newC] < (l-1, rt):
          queue.append((newR, newC, l-1, rt))
          visited[newR][newC] = (l-1, rt)
      

    
    if rt > 0:
      newR = r
      newC = c+1

      if inbound(newR, newC) and graph[newR][newC] != "*":
        if visited[newR][newC] == (-1, -1):
          counts += 1
        if visited[newR][newC] < (l, rt-1):
          queue.append((newR, newC, l, rt-1))
          visited[newR][newC] = (l, rt-1)
      
  print(counts+1)

T = 1
for _ in range(T):
  main()