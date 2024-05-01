n = int(input())
nums = list(map(int, input().split()))

left = 0
ans = []

while left < n:
    right = left + 1
    temp = []
    minVal = float('inf')
    minIdx = -1
    
    while right < n:
        if nums[right] < nums[left]:
            if minVal > nums[right]:
                minVal = nums[right]
                minIdx = right
        
        right += 1
            
    if minIdx > 0:
        right = minIdx
        temp.append(left)
        temp.append(minIdx)
    
        nums[right], nums[left] = nums[left], nums[right]
    
    if temp:
        ans.append(temp)
        
    left += 1

if ans:    
    print(len(ans))
    for idx in ans:
        print(*idx)

else:
    print(0)
    