class Node:
    def __init__(self,data):
        self.next=None
        self.data=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return

        last=self.head
        while last.next:
            last=last.next
        last.next=new_node

    def insert_at(self, index,data):
        new_node=Node(data)
        if index==0:
            new_node.next=self.head
            self.head=new_node
            return


