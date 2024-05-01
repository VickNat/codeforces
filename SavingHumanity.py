t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    arr = list(map(list, input().split()))
    
    for itr in range(m):
        
        idx = 0
        while idx < len(arr[0]):
            if arr[0][idx] == '1':
                
                if idx + 1 < n and arr[0][idx+1] == '0':
                    if idx + 2 == n:
                        arr[0][idx + 1] = '1'
                    elif idx + 2 < n and arr[0][idx + 2] != '1':
                        arr[0][idx + 1] = '1'

                
                if idx - 1 >= 0 and arr[0][idx - 1] == '0':
                    if idx - 2 < 0:
                        arr[0][idx - 1] = '1'
                    elif idx - 2 >= 0 and arr[0][idx - 2] != '1':
                        arr[0][idx - 1] = '1'
                    
                idx += 2
            idx += 1
        
    print("".join(arr[0]))
                
