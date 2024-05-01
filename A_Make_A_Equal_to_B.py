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
  N = InputInt()
  a = InputList()
  b = InputList()
  counts = defaultdict(int)

  if a == b:
    return 0

  for val in a:
    counts[val] += 1
  
  ans2 = 0
  for i in range(N):
    if a[i] != b[i]:
      ans2 += 1
  
  ans = 1
  for val in b:
    if counts[val] == 0:
      ans += 1
      counts[1-val] -= 1
    else:
      counts[val] -= 1
  
  return min(ans, ans2)


T = InputInt()
for _ in range(T):
  print(main())