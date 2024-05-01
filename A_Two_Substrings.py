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
  string = InputStr()
  ab = False
  ba = False
  
  for i in range(1, len(string)-1):
    if string[i] == "B":
      if string[i-1] == "A" and string[i+1] != "A":
        ab = True
        if ba:
          break
      if string[i-1] != "A" and string[i+1] == "A":
        ba = True
        if ab:
          break
        
  if len(string) > 3:
    if string[:2] == "BA":
      ba = True
    if string[len(string)-2:] == "AB":
      ab = True
  
  if ab and ba:
    print("YES")
  else:
    print("NO")
      

main()