import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
    N = InputInt()
    sieve = [True]*(N+1)
    sieve[0] = sieve[1] = False
    ptr = 2

    while ptr*ptr <= N:
      if sieve[ptr]:
        d = ptr*2

        while d <= N:
          sieve[d] = False
          d += ptr
        
      ptr += 1

    print(sieve)
    
main()