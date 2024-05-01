import math
from collections import defaultdict
from collections import Counter
from collections import deque

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  N, M = InputIterables()
  a, b = InputIterables()
  graph = [[] for _ in range(N)]
  queue = deque([a])
  prevNodes = defaultdict(int)
  prevNodes[a] = None
  visited = set()
  visited.add(a)
  flag = True

  for _ in range(M):
    node1, node2 = InputIterables()

    graph[node1-1].append(node2)
    graph[node1-1] = list(set(graph[node1-1]))

    graph[node2-1].append(node1)
    graph[node2-1] = list(set(graph[node2-1]))
  
  while queue:
    if not flag:
      break

    size = len(queue)

    for _ in range(size):

      node = queue.popleft()

      for elm in graph[node-1]:
        if elm not in visited:
          visited.add(elm)
          prevNodes[elm] = node
          queue.append(elm)
        
        if elm == b:
          flag = False

  if flag:
    print(-1)
  else:
    path = [b]
    val = b

    while prevNodes[val]:
      path.append(prevNodes[val])
      val = prevNodes[val]
    
    print(len(path)-1)
    print(*reversed(path))

main()

