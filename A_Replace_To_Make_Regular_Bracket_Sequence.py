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
  s = InputStr()
  stack = []
  counts = 0
  opening = "<{[("
  closing = ">}])"
 
  openCount = 0
  closeCount = 0
  openDict = defaultdict(int)
  closeDict = defaultdict(int)
 
  for c in s:
    if c in opening:
      openCount += 1
      openDict[c] += 1
    else:
      closeCount += 1
      closeDict[c] += 1
  
  if openCount != closeCount:
    return "Impossible"
 
  # for c in openDict.keys():
  #   if c == "<":
  #     counts += abs(openDict[c]-closeDict[">"])
  #   elif c == "{":
  #     counts += abs(openDict[c]-closeDict["}"])
  #   elif c == "(":
  #     counts += abs(openDict[c]-closeDict[")"])
  #   else:
  #     counts += abs(openDict[c]-closeDict["]"])
 
  i = 0
 
  while i < len(s):
    flag = False
    while i < len(s) and s[i] in opening:
      stack.append(s[i])
      i += 1
      flag = True
    
    while stack and i < len(s) and s[i] in closing:
      if (stack[-1] == "<" and s[i] != ">") or (stack[-1] == "{" and s[i] != "}") or (stack[-1] == "[" and s[i] != "]") or (stack[-1] == "(" and s[i] != ")"):
        counts += 1
      
      stack.pop()
      i += 1
      flag = True
    
    if not flag:
      i += 1
    
  if stack:
    return "Impossible"
  
  return counts
 
 
 
print(main())