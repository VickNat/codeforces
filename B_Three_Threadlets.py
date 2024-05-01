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
  arr = sorted(InputList())
  
  if arr[0] == arr[2]:
    return "YES"
  elif arr[0] == arr[1] and (arr[0]*3 == arr[2] or arr[0]*2 == arr[2]):
    return "YES"
  elif arr[0]*2 == arr[1] and arr[1] == arr[2]:
    return "YES"
  elif arr[0]*2 == arr[1] and arr[0]*3 == arr[2]:
    return "YES"
  elif arr[0] == arr[1] and arr[0]*4 == arr[2]:
    return "YES"
  else:
    return "NO"

T = InputInt()
for _ in range(T):
  print(main())