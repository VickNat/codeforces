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
  n, m = InputList()
  cities = InputList()
  towers = InputList()
  ans = -float('inf')
  cur = 0

  for i in range(len(cities)):
    temp = float('inf')

    for j in range(cur, len(towers)):
      if abs((towers[j]) - (cities[i])) > temp:
        break
      
      temp = abs((towers[j]) - (cities[i]))
      cur = j
    
    ans = max(ans, temp)
  
  print(ans)

main()