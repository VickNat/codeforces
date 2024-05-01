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
  weights = []
  graph = defaultdict(list)
  visited = set()
  ans = ""
  start = False

  for _ in range(3):
    weights.append(InputStr())
  
  for weight in weights:
    if weight[1] == '>':
      graph[weight[0]].append(weight[-1])
    elif weight[1] == '<':
      graph[weight[-1]].append(weight[0])
  
  for key, val in graph.items():
    if len(val) == 2:
      start = key
      break

  def dfs(idx):
    nonlocal ans
    if idx not in graph:
      ans += idx
      return      

    for elm in graph[idx]:
      if elm not in visited:
        visited.add(elm)
        dfs(elm)
    
    ans += idx
  
  if not start:
    print("Impossible")
  else:
    dfs(start)
    print(ans)

main()