
# Python Code: Insert Node at Specific Position in a Singly Linked List
class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

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

    # Special case: inserting at the head (index 0)

    # If the index is 0, we’re inserting at the beginning.
    # The new node’s next points to the current head.
    # Then we update self.head to point to the new node.
    def insert_at(self, index,data):
        new_node=Node(data)
        if index==0:
            new_node.next=self.head
            self.head=new_node
            return

    # Traverse to the node before the target index
        current=self.head
        count=0
        while current and count < index-1:
            current=current.next
            count +=1
        # check for valid index
        if not current:
            raise IndexError("Index out of bounds")

        new_node.next=current.next
        current.next=new_node

    def display(self):
        current =self.head
        while current:
            print(current.data, end=' -> ')
            current=current.next
        print ('None')



# Example usage
ll = LinkedList()
ll.append(5)
ll.append(10)
ll.append(15)
ll.append(20)

print("Before insertion:")
ll.display()

ll.insert_at(2, 30)  # Insert 30 at index 2

print("After insertion:")
ll.display()


