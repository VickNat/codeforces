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
  N, M = InputIterables()

  graph = defaultdict(list)
  levels = 0
  queue = deque()
  visited = set()
  x = 0
  y = 0

  for _ in range(M):
    a, b = InputIterables()

    graph[a].append(b)
    graph[b].append(a)
  
  for key, val in graph.items():
    if len(val) == 1:
      queue.append(key)
      visited.add(key)
      y += 1

  while queue:
    size = len(queue)
    flag = False

    for _ in range(size):
      cur = queue.popleft()

      if levels == 0:
        queue.append(graph[cur][0])
        visited.add(graph[cur][0])
      elif levels == 1:
        for elm in graph[cur]:
          if elm not in visited and len(graph[elm]) > 1:
            queue.append(elm)
            visited.add(elm)
            break
      else:
        for elm in graph[cur]:
          x += 1
          visited.add(elm)
        flag = True
        break
    if flag:
      break
    levels += 1
    
  print(x, y//x)






T = InputInt()
for _ in range(T):
  main()