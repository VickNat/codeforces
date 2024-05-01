testCases = int(input())

for test in range(testCases):
    size = int(input())
    candies = list(map(int, input().split()))
    
    alice = 0
    bob = size - 1
    totalCounts = 0
    weightA = candies[alice]
    weightB = candies[bob]
    
    while alice < bob:
        if weightA > weightB:
            bob -= 1
            weightB += candies[bob]

        elif weightA < weightB:
            alice += 1
            
            weightA += candies[alice]
        elif weightA == weightB:
            totalCounts = (size - bob) + (alice + 1)
            
            alice += 1
            # bob -= 1
            
            weightA += candies[alice]
            # weightB += candies[bob]

    print(totalCounts)