from collections import defaultdict , deque
import bisect
import sys

test = int(input())
for _ in range(test):
    graph = defaultdict(list)
    n = int(input())
    ans = [0] * (n + 1)
    for idx in range(2 , n + 1):
        start , a , b = map(int , input().split())
        graph[start].append((idx , a , b))
    
    queue = deque()
    queue.append((1 , 0 , [0] ))
    
    while queue:
        vertix , a , b  = queue.popleft()
        
        
        for node , x , y  in graph[vertix]:
            x += a
            mem = b + [b[-1] + y]
            index = bisect.bisect_left(mem , x)
            if index >= len(mem) or mem[index] > x:
                index -= 1
            ans[node] = index    
            queue.append((node , x , mem ))
    temp = []
    for i in range(2 , n + 1):
        temp.append(ans[i])
    print(*temp)