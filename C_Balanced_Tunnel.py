n = int(input())

ptr = 0

entry = list(map(int, input().split()))
exit = list(map(int, input().split()))

fine = 0
outSide = set()
for car in entry:
    while ptr < n and car not in outSide and exit[ptr] != car:
        outSide.add(exit[ptr])
        fine += 1
        ptr += 1
    
    ptr += 1

    

print(fine)