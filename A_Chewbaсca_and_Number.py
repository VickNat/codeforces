x = str(input())
ptr = 0
ans = ''

while ptr < len(x):
  if ptr == 0 and x[ptr] == '9':
    ans += x[ptr]
    ptr += 1
    continue
  if 9-int(x[ptr]) < int(x[ptr]):
    ans += str(9-int(x[ptr]))
  else:
    ans += x[ptr]
  ptr += 1

print(ans)
