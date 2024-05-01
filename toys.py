from collections import defaultdict

size, toys = list(map(int, input().split()))

costs = list(map(int, input().split()))
costs.sort()

toyList = defaultdict(int)

for _ in range(toys):
    toy = str(input())
    toyList[toy] += 1

# print(toyList)

minPtr = 0
maxPtr = size-1
minCost = 0
maxCost = 0


for t in toyList:
    minCost += toyList[t] * costs[minPtr]
    maxCost += toyList[t] * costs[maxPtr]
    minPtr += 1
    maxPtr -= 1

print(minCost, maxCost)