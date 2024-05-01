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
  sizeA = len(a)
  sizeB = len(b)
  ans = True

  i = 0
  j = 0

  while i < sizeA and j < sizeB:
    if a[i] == '-' or b[j] == '-':
      break
    if a[i] != b[j]:
      ans = False
      break
    
    i += 1
    j += 1
  
  i = sizeA-1
  j = sizeB-1

  while ans and i >= 0 and j >= 0:
    if a[i] == '-' or b[j] == '-':
      break
    if a[i] != b[j]:
      ans = False
      break
    
    j -= 1
    i -= 1
  
  if ans:
    print("YES")
  else:
    print("NO")

main()