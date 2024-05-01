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
  arr = InputList()
  nums = list(set(arr))
  nums.sort()
  
  ans = len(nums)

  for i in range(1, len(nums)):
    if nums[i]-nums[i-1] <= 1:
      ans -= 1
  
  if ans == 1:
    print("YES")
  else:
    print("NO")


T = InputInt()
for _ in range(T):
  main()