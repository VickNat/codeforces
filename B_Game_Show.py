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
  k, n = InputList()
  arr = InputList()
  max_ = 0

  for i in range(n):
    left = k
    temp = arr[i]
    div = 2

    while temp > 1:
      if temp % div == 0:
        break
      
      div += 1
    # print(div)
    far = 0
    while far < n:
      num = arr[far]
      if num%div == 0:
        far += 1
        continue

      if left - num < 0:
        break
      
      far += 1
      left -= num
    
    max_ = max(max_, far)
  
  print(max_)
    

T = 1
for _ in range(T):
  main()