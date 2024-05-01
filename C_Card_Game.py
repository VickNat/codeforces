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
  n = InputInt()
  mati = list(reversed(InputSortedList()))
  ibsa = list(reversed(InputSortedList()))
  ans = 0

  i = 0
  m = 0

  while i < len(ibsa):
    if mati[m] > ibsa[i]:
      ibsa.pop()
      m += 1
      ans -= 1
    else:
      m += 1
      i += 1
      ans += 1
  
  if ans > 0:
    print("YES")
  else:
    print("NO")

main()