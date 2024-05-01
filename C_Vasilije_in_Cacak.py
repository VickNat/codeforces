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
  N, K, X = InputList()

  max_ = K*(N-K+1 + N)//2
  min_ = K*(1+K)//2

  if min_ <= X <= max_:
    print("YES")
  else:
    print("NO")

T = InputInt()
for _ in range(T):
  main()