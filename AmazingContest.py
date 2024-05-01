size = int(input())

counts = 0

contest = list(map(int, input().split()))

maxScore = 0
minScore = 0

for idx in range(len(contest)):
    if idx == 0:
        maxScore = contest[idx]
        minScore = contest[idx]
    elif contest[idx] > maxScore:
        maxScore = contest[idx]
        counts += 1
    elif contest[idx] < minScore:
        minScore = contest[idx]
        counts += 1
    else:
        continue

print(counts)