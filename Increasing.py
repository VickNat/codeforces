testCases = int(input())

for tests in range(testCases):
    size = int(input())
    array = list(map(int, input().split()))
    
    answer = "YES"
    
    array.sort()
    
    for idx in range(1, len(array)):
        if array[idx] == array[idx-1]:
            answer = "NO"
            break
    
    print(answer)