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
  a, b = InputStr().split(" ")
  lettersB = defaultdict(int)

  for i in range(len(b)):
    lettersB[b[i]] += 1
  
  longestSubstrA = 0

  for i in range(min(len(a), len(b))):
    if lettersB[a[i]] > 0:
      lettersB[a[i]] -= 1
      longestSubstrA += 1
    else:
      break

  print(longestSubstrA)

T = InputInt()
for _ in range(T):
  main()