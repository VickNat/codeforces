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

  left = 1
  right = 2000000000

  while left != right:
    mid = (left + right+1)//2
    
    temp = 0
    i = n//2

    while i < n:
      if mid-arr[i] > 0:
        temp += mid-arr[i]

      i += 1
      if temp > k:
        break
    
    if temp <= k:
      left = mid
    else:
      right = mid-1
    
  return left

T = 1
for _ in range(T):
  print(main())