size = int(input())

for index in range(size):
    result = []

    nums = list(map(int, input().split()))

    l = nums[0]
    r = nums[1]

    edge = r - (r % l)

    result.append(l)
    result.append(edge)

    print(*result)
