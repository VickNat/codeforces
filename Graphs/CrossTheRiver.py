import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
    N = InputInt()
    edges = []
    visited = [0]*N
    visited[0] = 1

    for _ in range(N):
      animals = InputList()
      edges.append(animals[1:])
    
    def dfs(idx):

      for edge in edges[idx]:
        idx2 = edge-1
        if visited[idx] == visited[idx2]:
          return False
        
        if visited[idx2] == 0:
          visited[idx2] = 3-visited[idx]

          if not dfs(idx2):
            return False

      return True
    
    if dfs(0):
      print(":)")
    else:
      print(":(")

main()