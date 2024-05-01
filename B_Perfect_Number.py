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
  ans = 19
  k = InputInt()

  counts = 1
  i = 28

  while i < 10000001:
    if counts == k:
      break
    ans = i
    counts += 1
    i += 9

  print(ans)


T = 1
for _ in range(T):
  main()