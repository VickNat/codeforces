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
  string = InputStr()
  ans = set()
  n = len(string)
  i = 0

  while i < n:
    if i+1 == n:
      ans.add(string[i])
    else:
      if string[i] != string[i+1]:
        ans.add(string[i])
      else:
        i += 1
    
    i += 1
    
  
  print("".join(sorted(list(ans))))

T = InputInt()
for _ in range(T):
  main()