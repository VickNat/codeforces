n = int(input())

for idx in range(n):
    word = str(input())
    firstWords = word[0] + word[1] + "... "

    stutter = firstWords + word + "?"
    print(stutter)