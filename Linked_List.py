#This program is to show the implementation of linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.head=None
    def insertend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            curr_node=self.head
            while curr_node.next!=None:
                curr_node=curr_node.next
            curr_node.next=new_node
    def printlist(self):
        curr_node=self.head
        while(curr_node):
            print(curr_node.data)
            curr_node=curr_node.next
l=Linked()
l.insertend(10)
l.printlist()
