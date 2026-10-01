class Node:
  def __init__(self, data):
      self.data = data
      self.next = None


class linkedlist:
  def __init__(self):
    self.head=None
    self.size=0


  def add(self,data):
    if self.head==None:
      self.head=Node(data)
      self.size+=1
      return
    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=Node(data)
    self.size+=1


  def traversal(self):
    cn=self.head
    while cn is not None:
      print(cn.data,end="->")
      cn=cn.next
    print(cn)


  def search(self,data):
    cn=self.head
    ind=0
    while cn is not None:
      if cn.data==data:
        print(f'element {data} is at {ind} index')
        return
      cn=cn.next
      ind+=1
    print('element not found')


  def length(self):
    return self.size

  
  def ins_beg(self,data):
    obj=Node(data)
    obj.next=self.head
    self.head=obj

  def del_beg(self):
    if self.head is None:
      return
    self.head=self.head.next

  def ins_pos(self,data,newnode):
    cn=Node(data)
    ind=0
    while cn.next is not None:
      cn.next=newnode
      return
ll=linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.traversal()
ll.search(30)
print(ll.length())
ll.ins_beg(5)
ll.traversal()
ll.del_beg()
ll.traversal()
ll.ins_pos(20,25)
ll.traversal()