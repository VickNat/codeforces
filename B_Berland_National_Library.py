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
  prefix = [0]*(n+1)
  beforeShutdown = defaultdict(int)

  for i in range(n):
    login = InputStr().split(" ")
    if login[0] == "+":
      prefix[i+1] += 1
      beforeShutdown[login[1]] = i+1
    elif login[0] == "-":
      if login[1] in beforeShutdown:
        prefix[i+1] -= 1
      else:
        prefix[0] += 1
        prefix[i+1] -= 1
    
  for i in range(1, n+1):
    prefix[i] += prefix[i-1]
  
  print(max(prefix))

T = 1
for _ in range(T):
  main()