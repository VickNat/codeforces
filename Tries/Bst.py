class node:
  def __init__(self, num):
    self.val = num
    self.right = None
    self.left = None

class BST:
  def __init__(self):
    self.root = node(num=0)

  def insert(self, num):
    root = self.root

    while root:
      if root.val > num:
        root = root.left
      else:
        root = root.right
    
    root = node(num)

  def arrayToBST(self, nums):
    for num in nums:
      self.insert(num)

  def inorder(self):
    root = self.root

    if root:
      root = root.left
      print(root.val)
      root = root.right

bst = BST()

for i in range(5):
  bst.insert(i)

bst.inorder()

