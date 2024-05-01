import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  N = InputInt()

  qR, qC = InputList()
  kR, kC = InputList()
  dR, dC = InputList()

  ans = "YES"

  if (kR < qR < dR) or (dR < qR < kR):
    ans = "NO"
  
  if (kC < qC < dC) or (dC < qC < kC):
    ans = "NO"
  
  print(ans)


main()