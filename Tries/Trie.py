class TrieNode:
  def __init__(self) -> None:
    self.children = {}
    self.endOfWord = 0

class Trie:
  def __init__(self):
        self.root=TrieNode()

  def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.endOfWord    

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True     