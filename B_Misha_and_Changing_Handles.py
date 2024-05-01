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
  children = defaultdict(str)
  N = InputInt()

  for i in range(N):
    par, child = InputStr().split()

    if par in children:
      temp = children[par]
      del children[par]
      children[child] = temp
    else:
      children[child] = par
  
  print(len(children))
  
  for child, par in children.items():
    print(par, child)


main()