import math

def theatre_square(n, m, a):
    flagstones_n = math.ceil(n / a)
    flagstones_m = math.ceil(m / a)

    total_flagstones = flagstones_n * flagstones_m

    return total_flagstones

n, m, a = map(int, input().split())

result = theatre_square(n, m, a)
print(result)