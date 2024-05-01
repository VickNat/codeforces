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
  N = InputInt()
  arr = InputSortedList()

  if arr[0]%2 == 0:
    odds = []

    for idx, elm in enumerate(arr):
      if elm%2 != 0:
        if not odds or odds[0] == elm:
          return False
        odds.append(elm)
  return True

T = InputInt()
for _ in range(T):
  ans = main()
  if ans:
    print("YES")
  else:
    print("NO")