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
  N = str(InputInt())
  size = len(N)
  zeros = 0
  cur = -1
  ans = float('inf')

  for idx in range(size-1, -1, -1):
    if N[idx] == '0':
      zeros += 1
      cur = idx
      break
  
  if zeros:
    for idx in range(cur-1, -1, -1):
      if N[idx] == '0' or N[idx] == '5':
        temp = size-2-idx
        ans = min(ans, temp)
        break
  
  cur = -1
  fives = 0

  for idx in range(size-1, -1, -1):
    if N[idx] == '5':
      fives += 1
      cur = idx
      break
  
  if fives:
    for idx in range(cur-1, -1, -1):
      if N[idx] == '2' or N[idx] == '7':
        temp = size-2-idx
        ans = min(ans, temp)
        break
  
  print(ans)

T = InputInt()
for _ in range(T):
  main()