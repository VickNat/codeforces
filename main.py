moves = 8
position = str(input())

alp = int(ord(position[0]))
num = int(position[-1])

alpTop = alp + 1
alpBottom = alp - 1
numRight = num + 1
numLeft = num - 1

if alpBottom < 97 and numLeft < 1:
    moves -= 5
elif alpBottom < 97 and numRight > 8:
    moves -= 5
elif alpTop > 104 and numLeft < 1:
    moves -= 5
elif alpTop > 104 and numRight > 8:
    moves -= 5
elif alpTop > 104:
    moves -= 3
elif alpBottom < 97:
    moves -= 3
elif numRight > 8:
    moves -= 3
elif numLeft < 1:
    moves -= 3

print(moves)