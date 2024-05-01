import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  N = InputInt()
  employees = []

  for _ in range(N):  
    employees.append(InputInt())

  ans = max(employees)
  if ans == -1:
    ans = 1
  else:
    ans += 1
  
  print(ans)

main()