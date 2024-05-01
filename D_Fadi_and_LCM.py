import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  N = InputInt()
  factors = []
  ans = [1, N]

# We can optimize the factor finding technique upto only it's root and store both the divider and dividend
  for i in range(1, int(math.sqrt(N))+1):
    if N%i == 0:
      factors.append(N//i)
      factors.append(i)
  
  # Since bruteforcing to find the minimum possible value of max(a, b) exceeds time limit
  for a in factors:
    # we optimize it by only searching for the minimum possible value b that can give an lcm of N with an a
    b = N // a
    # if the gcd(a, b) == 1 it means their lcm is their product
    if math.gcd(a, b) == 1 and max(a, b) < max(ans):
      ans = [a, b]
  
  print(*ans)

main()