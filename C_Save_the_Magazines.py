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
  lids = InpStrToList()
  mags = InputList()

  ans = 0
  left = 0
  
  while left < N:
    minVal = mags[left] if lids[left] == "0" else 0
    curSum = mags[left]
    right = left+1
		
    while right < N and lids[right] == "1":
      minVal = min(minVal, mags[right])
      curSum += mags[right]
  
      right += 1
    
    ans += curSum-minVal

    left = right

  print(ans)


T = InputInt()
for _ in range(T):
  main()