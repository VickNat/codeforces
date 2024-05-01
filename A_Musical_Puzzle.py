import math
from collections import defaultdict
from collections import Counter
from collections import deque
import heapq

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))
def InpStrToList(): return list(input())

def main():
  n = InputInt()
  music = input()
  melodies = set()
  melodies.add(music[0:2])
  ptr = 2

  while ptr < n:
    temp = music[ptr-1] + music[ptr]
    melodies.add(temp)
    ptr += 1
  
  print(len(melodies))

T = InputInt()
for _ in range(T):
  main()