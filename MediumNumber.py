testCases = int(input())

for tests in range(testCases):
    integers = list(map(int, input().split()))
    
    integers.sort()
    
    print(integers[1])