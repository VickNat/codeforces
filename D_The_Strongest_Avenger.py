from functools import cache
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
  nums = list(map(int, list(input())))
  ans = 0

  @cache
  def dp(idx, sum_, length):
    nonlocal ans
    if sum_ == length:
      ans += 1
    
    if idx+1 < N:
      dp(idx+1, sum_+nums[idx+1], length+1)
    
  for i in range(N):
    dp(i, nums[i], 1)
  
  print(ans)


T = InputInt()
for _ in range(T):
  main()