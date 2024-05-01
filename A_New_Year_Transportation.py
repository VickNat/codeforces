import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  n, t = InputList()
  cells = InputList()

  ans = "NO"
  i = 0

  while i <= n-1:
    if i+1 == t:
      ans = "YES"
      break
    
    if i < n-1:
      i += cells[i]
    else:
      break

  print(ans)

main()