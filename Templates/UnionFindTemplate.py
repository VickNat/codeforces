# Author Vick

import math
from collections import defaultdict
from collections import Counter
from collections import deque
import heapq

class UnionFind:

  def __init__(self, length):
    self.length = length
    self.parent = {i : i for i in range(self.length)}
    self.size = {i : 1 for i in range(self.length)}


  def find(self, x):
    if x == self.parent[x]:
      return x
    
    self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
  
  def union(self, x, y):
    x_rep = self.find(x)
    y_rep = self.find(y)

    if x_rep != y_rep:
      if self.size[x_rep] < self.size[y_rep]:
        x_rep, y_rep = y_rep, x_rep
      
      self.parent[y_rep] = self.parent[x_rep]
      self.size[x_rep] += self.size[y_rep]
