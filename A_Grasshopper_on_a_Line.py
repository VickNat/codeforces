# import math
# from collections import defaultdict
# from collections import Counter
# from collections import deque
# import heapq

# def InputStr(): return input()
# def InputInt(): return int(input())
# def InputIterables(): return map(int, input().split())
# def InputList(): return list(map(int, input().split()))
# def InputSortedList(): return sorted(list(map(int, input().split())))
# def InpStrToList(): return list(input())

# def main():
#   N, K = InputIterables()
#   temp = N
#   ans = []

#   while temp%K == 0:
#     temp -= 1
  
#   ans.append(temp)
#   counts = 0

#   while temp < N or (counts%K == 0 and temp != N):
#     temp += 1
#     counts += 1
  
#   if counts:
#     ans.append(counts)
#   if temp != N:
#     ans.append(temp-N)

  
  
#   print(len(ans))
#   print(*ans)


# T = InputInt()
# for _ in range(T):
#   main()

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
def InpStrToList(): return list(input())

def main():
  N, K = InputIterables()
  temp = N
  ans = []

  if N%K == 0:
    ans.append(N-1)
    ans.append(1)
  else:
    ans.append(N)
  
  print(len(ans))
  print(*ans)


T = InputInt()
for _ in range(T):
  main()