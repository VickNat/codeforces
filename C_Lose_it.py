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
  n = InputInt()
  a = InputList()

  indices = {4: 1, 8: 2, 15: 3, 16: 4, 23: 5, 42: 6}

  cnt = [0] * 7

  for num in a:
    if num == 4:
      cnt[1] += 1
    else:
      pos = indices[num]
      if cnt[pos - 1] > 0:
        cnt[pos - 1] -= 1
        cnt[pos] += 1

  ans = n - (cnt[6] * 6)

  print(ans)

main()