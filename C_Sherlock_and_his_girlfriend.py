import math
from collections import defaultdict
from collections import Counter
from typing import List

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  N = InputInt()
  prime = [1]*(N+2)
  idx = 2

  while idx < N+2:
    if prime[idx] == 1:
      d = idx*2

      while d < N+2:
        prime[d] = 2
        d += idx
    
    idx += 1

  return prime

k = main()[2:]
print(len(set(k)))
print(*k)
