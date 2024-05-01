size = int(input())

for inp in range(size):
    song = list(map(str, input().split()))

    disk = dict()

    for word in range(len(song)):
        num = 0

        for letter in range(len(song[word])):
            if song[word][letter].isdigit():
                num = (num * 10) + int(song[word][letter])

        disk[num] = song[word]

    dictKeys = list(disk.keys())
    dictKeys.sort()
    sortedDict = {idx: disk[idx] for idx in dictKeys}

    # dict(sorted(disk.items()))

    # print(sortedDict)

    answer = []

    for index in range(1, len(disk) + 1):
        for let in range(len(disk[index])):

            if disk[index][let].isdigit():
                continue
            else:
                answer.append(disk[index][let])

        answer.append(" ")

    print("".join(answer))