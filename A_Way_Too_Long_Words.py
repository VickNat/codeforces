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
  word = InputStr()
  if len(word) <= 10:
    print(word)
  else:
    print(word[0]+str(len(word)-2)+word[-1])
  

T = InputInt()
for _ in range(T):
  main()