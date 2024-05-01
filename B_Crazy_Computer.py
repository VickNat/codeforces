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
  n, c = InputList()
  t = InputList()
  ans = [0]*n
  ans[0] = 1

  for i in range(1, n):
    if t[i]-t[i-1] > c:
      ans[i] = 1
    else:
      ans[i] = ans[i-1] + 1
  
  print(ans[-1])


main()