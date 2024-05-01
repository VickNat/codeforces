import sys, threading
sys.setrecursionlimit(10000)  # Setting a reasonable recursion limit
threading.stack_size(1 << 27)

from collections import defaultdict
from heapq import heappop, heappush

def inpNum():
    return int(input())

def inpSepNum():
    return map(int, input().split())

def inpNumList():
    return list(map(int, input().split()))
    
def f(n):
    return int(n)-1

n=int(input())
p=[0]+list(map(f,input().split()))
l=list(map(int,input().split()))

t=[float('inf')]*n
for i in range(n):
    if l[i]>=0:
        t[p[i]]=min(t[p[i]],l[i])

t=[t[i] if t[i]!=float('inf') else -1 for i in range(n)]
s=[l[i] if l[i]>=0 else t[i] for i in range(n)]
s=[s[p[i]] if s[i]<0 else s[i] for i in range(n)]

ans=[s[i]-s[p[i]] for i in range(n)]
ans[0]=l[0]

if any(i<0 for i in ans):
    print(-1)
else:
    print(sum(ans))