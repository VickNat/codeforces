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
  mati = InputRevSortedList()
  ibsa = InputRevSortedList()
  ans = 0

  i = 0
  m = 0
  swaps = []

  while m < n:
    if mati[m] <= ibsa[i]:
      i += 1
      m += 1
    else:
      if swaps:
        swaps.pop()
      else:
        swaps.append(mati[m])
        ans += 1
      m += 1
  
  print(ans)

main()