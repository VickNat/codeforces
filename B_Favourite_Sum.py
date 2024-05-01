import math
from collections import defaultdict
from collections import Counter
from itertools import accumulate

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  n, x = InputList()
  nums = InputSortedList()
  sum_ = 0
  minus = 0
  
  sum_ = (x*(x+1))//2

  left = -1
  right = n

  while left+1 < right:
    mid = left + (right-left)//2

    if nums[mid] <= x:
      left = mid
    else:
      right = mid
  
  minus = sum(nums[:left+1])
  
  print(sum_-(2*minus))


T = InputInt()
for _ in range(T):
  main()