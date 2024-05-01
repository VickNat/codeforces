testCases = int(input())

for tests in range(testCases):
    size = int(input())
    circle = list(map(int, input().split()))
    
    answer = "YES"
    counts = 0
    
    for idx in range(size):
        if idx+1 < size and abs(circle[idx] - circle[idx+1]) != 1:
            counts += 1
        elif idx == size -1 and abs(circle[idx] - circle[0]) != 1:
            counts += 1
        
    if counts > 1:
        answer = "NO"
    
    print(answer)
        

        '''
        rows, cols = list(map(int, input().split()))

check = []

for idx in range(rows):
    row = list(map(str, input().split()))
    
    for col in range(len(row)):
        if row[col] == "*":
            temp = []
            
            temp.append(row)
            temp.append(col)
            
            check.append(temp)
    
counts = 0

for j in check:
    
    r = j[0]
    c = j[1]
    temp = []
    
    r -= 1
    
    temp.append(r)
    temp.append(c)
    
    if temp not in check:
        r = j[0]
        c = j[1]
        
        temp[0] = r
        temp[1] = c
        continue
    
    r += 1
    temp[0] = r
    temp[1] = c
    
    if temp not in check:
        r = j[0]
        c = j[1]
        
        temp[0] = r
        temp[1] = c
        continue
    
    c += 1
    temp[0] = r
    temp[1] = c
    
    if temp not in check:
        r = j[0]
        c = j[1]
        
        temp[0] = r
        temp[1] = c
        continue
    
    c -= 1
    temp[0] = r
    temp[1] = c
    
    if temp not in check:
        r = j[0]
        c = j[1]
        
        temp[0] = r
        temp[1] = c
        continue
    
    counts += 1
    
if counts == 0:
    print("NO")
else:
    print("YES")
    
    
        '''