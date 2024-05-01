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
def InpStrToList(): return list(input())

def main():
  N = InputInt()
  string = InputStr()
  ans = 0
  start = 0

  for end in range(N):
    if string[end] != string[start]:
      ans = max(ans, end-start+1)
      start = end

  ans = max(ans, end-start+2)
  print(ans)

T = InputInt()
for _ in range(T):
  main()