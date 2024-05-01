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
  intervals = []
  max_ = 0

  for i in range(N):
    val = InputList()
    max_ = max(max_, max(val))
  
    intervals.append(val)
  
  prefixSum = [0]*(max_+1)
  for start, end in intervals:
    prefixSum[start] += 1
    prefixSum[end] -= 1

  for i in range(1, max_+1):
    prefixSum[i] += prefixSum[i-1]
    
  print(max(prefixSum))

T = InputInt()
for _ in range(T):
  main()