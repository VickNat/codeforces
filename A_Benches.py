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
  m = InputInt()
  max_ = -float('inf')
  nums = []

  for _ in range(n):
    nums.append(InputInt())
    max_ = max(max_, nums[-1])
  
  max_ += m

  while m > 0 and len(nums) > 1:
    nums.sort()
    m -= nums[1]-nums[0]+1
    nums[0] += nums[1]-nums[0]+1
    
    if m < 0:
      nums[0] += m
      
  
  if len(nums) > 1:
    print(max(nums), max_)
  else:
    print(max_, max_)

main()