n, a, b = list(map(int, input().split()))

stud = list(map(int, input().split()))

l = 0
r = 0
total = 0
counts = 0

for r in range(n):
    total += stud[r]

    if total >= a and total <= b:
        counts += 1

    if total > a and total <= b:
        tempL = l
        tempTot = total
        
        while tempL <= r:
            tempTot -= stud[tempL]
            
            if tempTot >= a and tempTot <= b:
                counts += 1

            tempL += 1
            
        
    if total > b:
    
        while total >= a and l <= r:
            total -= stud[l]
            if total >= a and total <= b:
                counts += 1
            l += 1

    if l > r:
        l -= 1
    
print(counts)