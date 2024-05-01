def dominoPiling(m, n):
    return (m * n) // 2

m, n = map(int, input().split())
result = dominoPiling(m, n)
print(result)