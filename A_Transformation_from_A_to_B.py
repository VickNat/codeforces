import math
from collections import defaultdict
from collections import Counter

def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))

def main():
  a, b = InputList()

  def dfs(val, path):
    if val > b:
      return [False, path + [val]]
    if val == b:
      return [True, path[:]]

    num1 = val*2
    num2 = (val*10) + 1

    ans1 = dfs(num1, path+[num1])
    ans2 = dfs(num2, path+[num2])

    if ans1[0]:
      return ans1
    if ans2[0]:
      return ans2
    
    return [False, path[:]]
  
  ans = dfs(a, [a])

  if ans[0]:
    print("YES")
    print(len(ans[1]))
    print(*ans[1])
  else:
    print("NO")

main()