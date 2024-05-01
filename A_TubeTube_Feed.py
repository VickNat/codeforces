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
  n, k = InputIterables()
  secs = InputList()
  ent = InputList()
  max_ = -1

  for idx in range(n):
    if secs[idx] <= k:
      if max_ == -1 or ent[idx] > ent[max_]:
        max_ = idx

    k -= 1
  
  if max_ == -1:
    print(-1)
  else:
    print(max_+1)

T = InputInt()
for _ in range(T):
  main()