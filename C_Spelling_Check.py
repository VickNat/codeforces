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
  a = InputStr()
  b = InputStr()
  N = len(a)
  M = len(b)

  if len(set(a)) == 1 or len(set(b)) == 1:
    ans = [i+1 for i in range(N)]
    print(len(a))
    print(*ans)
  else:
    ptr1 = 0
    ptr2 = 0
    ans = []
    while ptr1 < N and ptr2 < M:
      while ptr1 < N and a[ptr1] != b[ptr2]:
        ans.append(ptr1 + 1)
        ptr1 += 1
      
      ptr1 += 1
      ptr2 += 1
    
    if ptr2 < M:
      print(0)
    else:
      print(len(ans))
      print(*ans)


T = 1
for _ in range(T):
  main()