a, b, c = int(input().split())

countA = a+c
countB = b+c
answer = 0

if countA>countB:
  answer = countB+1
elif countA<countB:
  answer = countA+1
else:
  answer = countA

print(answer)