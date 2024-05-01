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
  arr = InputList()
  min_ = float('inf')
  minIdx = -1
  cur = 0

  start = 0
  for end in range(n):
    cur += arr[end]
    if end-start+1 < k:
      continue
    
    if end-start+1 > k:
      cur -= arr[start]
      start += 1

    if cur < min_:
      min_ = cur
      minIdx = start
  
  print(minIdx+1)

main()