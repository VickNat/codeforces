import math
from collections import defaultdict
from collections import Counter
from collections import deque
import heapq
import sys

def InputStr(): return input()
def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, sys.stdin.readline().rstrip().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))
def InputRevSortedList(): return list(reversed(sorted(list(map(int, input().split())))))
def InpStrToList(): return list(input())

def main():
  N, M, Q = InputList()
  distances = [[10**(14)]*(N) for _ in range(N)]
  queries = []
  
  for _ in range(M):
    a, b, c = InputList()
    if c < distances[a-1][b-1]:
      distances[a-1][b-1] = distances[b-1][a-1] = c

  for _ in range(Q):
    queries.append(InputList())
  
  for i in range(N):
    distances[i][i] = 0
  
  for k in range(N):
    for i in range(N):
      for j in range(i+1, N):
        newDist = distances[i][k]+distances[k][j] 
        if newDist < distances[i][j]:          
          distances[j][i] = distances[i][j] = newDist

  for i, j in queries:
    ans = distances[i-1][j-1] if distances[i-1][j-1] != 10**(14) else -1
    print(ans)
  
main()