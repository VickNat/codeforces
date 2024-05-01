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
  n, x, y = InputList()

  if n == 1:
    return 0

  if x == y:
    return (n-1)*x

  ans = 0

  for i in range(y):
    ans += x
  
  for i in range(x):
    ans += y
  
  ans = min(ans, min(x, y)*(n-1), )
  
  return ans

T = 1
for _ in range(T):
  print(main())