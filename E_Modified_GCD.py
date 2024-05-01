import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
    a, b = InputSortedList()
    N = InputInt()
    factors = set()
    val = math.gcd(a, b)

    for i in range(1, int(val**(0.5))+1):
      if val%i == 0:
        factors.add(val//i)
        factors.add(i)

    factors = sorted(list(factors))

    for _ in range(N):
      ans = -1
      l, r = InputList()

      if l > min(a, b):
        print(ans)
        continue
      
      left = 0
      right = len(factors)

      while left+1 < right:
        mid = left + (right-left)//2

        if factors[mid] <= r:
          left = mid
        else:
          right = mid
      
      if l <= factors[left] <= r:
        ans = factors[left]
      print(ans)
    
main()