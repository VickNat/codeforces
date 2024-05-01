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
  s1 = InputStr()[::-1]
  s2 = InputStr()[::-1]

  length = min(len(s1), len(s2))
  ptr = 0

  while ptr < length:
    if s1[ptr] != s2[ptr]:
      break
    ptr += 1
  
  print((len(s1)-ptr) + (len(s2)-ptr))
    

main()