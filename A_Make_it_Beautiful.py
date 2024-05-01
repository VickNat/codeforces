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
  size = InputInt()
  arr = InputRevSortedList()

  if size > 2 and arr[0] == arr[1]:
    arr[1], arr[-1] = arr[-1], arr[1]

  cur = 0
  flag = True

  for i, num in enumerate(arr):
    if num == cur:
      flag = False
      break
    
    cur += num
  
  if flag:
    print("YES")
    print(*arr)
  else:
    print("NO")

T = InputInt()
for _ in range(T):
  main()