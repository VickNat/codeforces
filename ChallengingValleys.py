testCases = int(input())

for tests in range(testCases):
    size = int(input())
    valley = list(map(int, input().split()))
    
    idx = 0
    check = -1
    flag = 0

    
    for idx in range(size-1):
        if valley[idx] < valley[idx + 1]:
            check = idx
            break
    
    if check != -1:
        while check < size -1:
            if valley[check] > valley[check + 1]:
                flag = 1
                break
            
            check += 1
        
    if flag == 1:
        print("No")
    else:
        print("Yes")