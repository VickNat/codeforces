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
  N, M = InputList()
  x = InputStr()
  a = InputStr()

  chars = set()

  for c in x:
    chars.add(c)
  
  for c in a:
    if c not in chars:
      return -1
  
  counts = 0
  
  while len(x) < 25:
    if a in x:
      return counts
    
    x += x
    counts += 1
  
  if a in x:
    return counts
  return -1

T = InputInt()
for _ in range(T):
  print(main())