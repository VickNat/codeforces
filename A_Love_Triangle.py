import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  N = InputInt()
  nums = InputList()
  ans = "NO"
  
  for i in range(N):
    val = nums[nums[nums[nums[i]-1]-1]-1]

    if val == nums[i]:
      ans = "YES"
      break
  
  print(ans)

main()



