import math
from collections import defaultdict
from collections import Counter
from collections import deque
import heapq

def InputStr(): return input()
def InputInt(): return int(input())
def InputIterables(): return map(int, input().split())
def InputList(): return list(map(int, input().split()))
def InputSortedList(): return sorted(list(map(int, input().split())))
def InputRevSortedList(): return list(reversed(sorted(list(map(int, input().split())))))
def InpStrToList(): return list(input())

class TrieNode:
  def __init__(self) -> None:
    self.children = [None]*2
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.root=TrieNode()

  def insert(self, num) -> None:
    cur=self.root

    i = 31
    while i >= 0:
      idx = (num >> i) & 1

      if cur.children[idx] == None:
        cur.children[idx] = TrieNode()

      cur = cur.children[idx]
      i -= 1  

  def startsWith(self, num):
    cur=self.root
    ans = 0

    i = 31
    while i >= 0:
      bit = (num >> i) & 1
      if cur.children[bit^1] != None:
        cur = cur.children[bit^1]
        ans += 1 << i
      else:
        cur = cur.children[bit]
      
      i -= 1
    
    return ans

def main():
  N = InputInt()
  nums = InputList()
  ans = 0
  trie = Trie()

  trie.insert(nums[0])
  for num in nums[1:]:
    ans = max(ans, trie.startsWith(num))
    trie.insert(num)
  
  print(ans)

T = InputInt()
for _ in range(T):
  main()