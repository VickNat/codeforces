import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
    N = InputInt()
    nums = InputSortedList()
    twoCounts = 0
    max_ = 0
    sum_ = 0

    for idx in range(N):
      while nums[idx]%2 == 0:
        nums[idx] //= 2
        twoCounts += 1
    
      max_ = max(max_, nums[idx])
      sum_ += nums[idx]
    
    sum_ -= max_
    sum_ += max_*(2**twoCounts)
    return sum_

T = InputInt()
for _ in range(T):
    print(main())
