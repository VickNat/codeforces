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
def InpStrToList(): return list(input())

def main():
  binary = InpStrToList()
  N = len(binary)
  temp = "1"

  for idx in range(N-1, -1, -1):
    if binary[idx] == "?":
      binary[idx] = temp
    else:
      temp = binary[idx]

  print("".join(binary))

T = InputInt()
for _ in range(T):
  main()