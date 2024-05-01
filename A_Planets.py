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
  N, C = InputIterables()
  planets = Counter(InputList())
  ans = 0

  for key, val in planets.items():
    if val >= C:
      ans += C
    else:
      ans += val
  
  print(ans)

T = InputInt()
for _ in range(T):
  main()