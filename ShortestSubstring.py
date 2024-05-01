testCases = int(input())

for tests in range(testCases):
    nums = input()
    size = len(nums)
    
    left = 0
    right = 1
    counts = 0
    
    
    while left < size and left <= right:
        substr = nums[left:right + 1]
        
        if "1" in substr and "2" in substr and "3" in substr:
            if counts == 0:
                counts = len(substr)
            else:
                counts = min(counts, len(substr))
            left += 1
        elif right >= size:
            left += 1
        else:
            right += 1
    
    print(counts)