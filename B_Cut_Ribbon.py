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
    n, a, b, c = InputList()
    valid = [a, b, c]

    dp = defaultdict(int)
    dp[0] = 1

    for cur in range(min(valid), n + 1):
        max_ = 0
        for val in valid:
            if cur - val >= 0:
                max_ = max(max_, dp[cur - val])
        
        if max_ > 0:
            max_ += 1
        
        dp[cur] = max_

    ans = dp[n]
    return ans - 1

T = 1
for _ in range(T):
  ans = main()
  if ans < 0:
    ans = 0
  print(ans)