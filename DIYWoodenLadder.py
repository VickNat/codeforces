testCases = int(input())

for tests in range(testCases):
    size = int(input())
    planks = list(map(int, input().split()))
    
    planks.sort()
    
    ladder = []
    steps = 0
    
    if len(planks) <= 2:
        print(steps)
    else:
        ladder.append(planks[-1])
        ladder.append(planks[-2])
        
        for step in range(size - 2):
            if step+1 == ladder[1]:
                break
            else:
                steps += 1
        
        print(steps)