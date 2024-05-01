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
  s = InputInt()
  ans = float('inf')

  def findSum(cur, sum_, idx):
    nonlocal ans
    
    if sum_ > s:
      return
    if sum_ == s:
      val = int("".join(cur))
      ans = min(val, ans)
      return
    if idx > 9:
      return
    
    findSum(cur+[str(idx)], sum_+idx, idx+1)
    findSum(cur, sum_, idx+1)
  
  findSum([], 0, 1)
  print(ans)

T = InputInt()
for _ in range(T):
  main()