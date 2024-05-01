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
  N, M = InputList()
  chairs = defaultdict(int)
  moves = []

  for i in range(N):
    row, col = InputList()
    chairs[(row, col)] += 1
  
  for i in range(M):
    pos = tuple(InputList())
    moves.append(pos)
    
  for ranges in moves:
    inside = 0
    rowi, coli, rowj, colj = ranges
    for row, col in chairs:
      if rowi <= row <= rowj and coli <= col <= colj:
        inside += chairs[(row, col)]
    
    print(inside)


main()