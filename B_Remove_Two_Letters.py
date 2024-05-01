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

MOD = (int)(1e9+7)

def main():
  N = InputInt()
  s = InputStr()

  if N == len(set(s)):
    return N-1
  if len(set(s)) == 1:
    return 1

  left = 1

  for i in range(2, N):
    if s[i-2] != s[i]:
      left += 1
     
  return left


T = InputInt()
for _ in range(T):
  print(main())