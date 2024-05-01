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
    self.children = {}
    self.endOfWord = False

class Trie:
  def __init__(self):
    self.root=TrieNode()
    self.counts = 0

  def insert(self, word: str) -> None:
    cur=self.root
    for c in word:
      if c not in cur.children:
        cur.children[c]=TrieNode()

      cur=cur.children[c]
    cur.endOfWord=True   

  def startsWith(self, prefix: str) -> bool:
    cur=self.root
    for idx in range(len(prefix)):
      c = prefix[idx]

      if c not in cur.children:
        return idx
      
      cur=cur.children[c]
    return len(prefix)
    

def main():
  N = InputInt()
  words = []

  for i in range(N):
    word = InputStr()
    words.append(word)

  for i in range(N):
    trie = Trie()
    word = words[i]
    for j in range(N):
      check = words[j]
      if i != j:
        trie.insert(check)

    print(trie.startsWith(word))

main()