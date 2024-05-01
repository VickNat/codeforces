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
  n = InputInt()
  arr = InputList()
  ans = arr.count(0)
  
  for idx in range(n):
    num = arr[idx]
    if idx+1 < n:
      if num == 2 or num == 1:
        if arr[idx+1] == num:
          ans += 1
          idx += 1
  
  start = 0
  for end in range(n):
    while start < end and (arr[start] != 2 and arr[start] != 1):
      start += 1
    
    if arr[end] != 3 and end - 1 == start:
      start = end
      continue

    if (arr[start] == 2 and arr[end] == 1) or (arr[start] == 1 and arr[end] == 2):
      if (end - start - 1)%2 != 0:
        ans += 1
        start = end + 1

  print(ans)

main()