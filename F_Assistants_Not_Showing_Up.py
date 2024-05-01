import itertools

n, m = list(map(int, input().split()))

prefixSum = [0]*(n+1)
for _ in range(m):
  a, b = list(map(int, input().split()))
  prefixSum[a] += 1
  prefixSum[b+1] -= 1

sum_ = list(itertools.accumulate(prefixSum))
sum_.pop()

ans = "NO"
if 0 in sum_:
  ans = "YES"

print(ans)