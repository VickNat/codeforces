import math
from collections import defaultdict
from collections import Counter
from itertools import accumulate

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  n, m, k = InputIterables()
  players = []
  friends = 0
  
  for _ in range(m+1):
    players.append(InputInt())
  
  fado = players.pop()
  
  for p in players:
    val = bin(fado^p)[2:]
    counts = val.count('1')
    
    if counts <= k:
      friends += 1
  
  print(friends)

main()