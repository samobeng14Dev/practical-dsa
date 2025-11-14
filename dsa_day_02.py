
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
    def insert(self,index,data):
        new_node=Node(data)
        if index==0:
            new_node.next=self.head
            self.head=new_node

    def insert_at(self, index, data):
        new_node = Node(data)  # Step 1: Create a new node with the given data

        # Special case: inserting at the head (index 0)
        if index == 0:
            new_node.next = self.head  # Link new node to the current head
            self.head = new_node  # Update head to point to the new node
            return

        # Step 2: Traverse to the node just before the target index
        current = self.head  # Start from the head
        count = 0  # Position counter
        while current and count < index - 1:
            current = current.next  # Move to the next node
            count += 1  # Increase step count

        # Step 3: If current is None, it means index is out of bounds
        if not current:
            raise IndexError("Index out of bounds")

        # Step 4: Rewire pointers to insert the new node
        new_node.next = current.next  # New node points to the next node in the chain
        current.next = new_node  # Current node now points to the new node

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


