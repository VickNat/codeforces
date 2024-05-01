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
  letter = InputStr()
  n = len(letter)
  ans1 = 0
  cur = 0
  ptr = n-1

  while ptr >= 0:
    if letter[ptr].isupper():
      cur += 1
    elif letter[ptr].islower():
      ans1 += cur
      cur = 0
    ptr -= 1
  
  ptr = 0
  ans2 = 0
  cur = 0
  while ptr < n:
    if letter[ptr].islower():
      cur += 1
    elif letter[ptr].isupper():
      ans2 += cur
      cur = 0
    ptr += 1
  
  print(min(ans1, ans2))

main()