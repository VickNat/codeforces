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
  n, k = InputList()
  arr = InputSortedList()

  max_ = 1
  counts = 1

  for i in range(1, n):
    if abs(arr[i]-arr[i-1]) <= k:
      counts += 1
    else:
      counts = 1
    max_ = max(max_, counts)

  print(n-max_)


T = InputInt()
for _ in range(T):
  main()