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
    N, K = InputIterables()
    nums = InputList()

    ans = 0
    threshold = nums[K-1]

    for score in nums:
        if score >= threshold and score > 0:
            ans += 1

    print(ans)

main()