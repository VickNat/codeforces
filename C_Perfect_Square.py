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
  N = InputInt()
  matrix = []

  for _ in range(N):
    matrix.append(InpStrToList())
  
  ans = 0
  
  for i in range(N//2):
    for j in range(N//2):
      temp = []
      temp.append(matrix[i][j])
      temp.append(matrix[N-1-j][i])
      temp.append(matrix[N-1-i][N-1-j])
      temp.append(matrix[j][N-1-i])

      temp.sort()
      ans += 3*ord(temp[3])-ord(temp[0])-ord(temp[1])-ord(temp[2])
  
  print(ans)
      


T = InputInt()
for _ in range(T):
  main()