size = int(input())

array = list(map(int, input().split()))

sortedArray = sorted(array)
ans = []
counts = 0

l = 0

if sortedArray == array:
    counts += 1
    ans.append(array[0])
    ans.append(array[0])
else:
    for l in range(size):
        r = l+1
    
        while r < size:
            temp = []
        
            reverseCheck = list(reversed(array[l:r+1]))
        
            temp = array[:l] + reverseCheck[:] + array[r+1:]
            # print(*temp)
        
            if temp == sortedArray:
                counts += 1
                t = array[l:r+1]
                ans.append(array[l])
                ans.append(array[r])
                r+= 1
                break
            else:
                r += 1


if counts > 0:
    print("yes")
    ans.sort()
    print(*ans)
else:
    print("no")