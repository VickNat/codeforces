class Node:
  def __init__(self, dataval):
    self.dataval = dataval
    self.nextval = None

class SLinkedList:
  def __init__(self):
    self.headval = None
  
  def listPrint(self):
    printval = self.headval

    while printval is not None:
      print(printval.dataval)
      printval = printval.nextval

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.headval.nextval = e2
e2.nextval = e3



