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
  a = InputStr()
  b = InputStr()

  if len(a) != len(b):
    print(max(len(a), len(b)))
  else:
    if a == b:
      print(-1)
    else:
      print(len(a))

T = 1
for _ in range(T):
  main()