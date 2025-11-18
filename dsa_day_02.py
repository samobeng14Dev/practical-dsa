# -------------------------------
# Node class: represents a single element in the linked list
# -------------------------------
class Node:
    def __init__(self, data):
        self.data = data      # Store the value of the node
        self.next = None      # Pointer to the next node (initially None)


# -------------------------------
# LinkedList class: manages the chain of nodes
# -------------------------------
class LinkedList:
    def __init__(self):
        self.head = None      # Head points to the first node in the list

    # -------------------------------
    # Append method: add a new node at the end of the list
    # -------------------------------
    def append(self, data):
        new_node = Node(data)   # Create a new node

        # Case 1: If list is empty, new node becomes head
        if not self.head:
            self.head = new_node
            return

        # Case 2: Otherwise, traverse to the last node
        last = self.head
        while last.next:        # Keep moving until last.next is None
            last = last.next

        # Link the last node to the new node
        last.next = new_node

    # -------------------------------
    # Insert_at method: insert a node at a specific index
    # -------------------------------
    def insert_at(self, index, data):
        new_node = Node(data)   # Step 1: Create the new node

        # Step 2: Handle insertion at the head
        if index == 0:
            new_node.next = self.head   # Link new node to current head
            self.head = new_node        # Update head to new node
            return

        # Step 3: Traverse to the node just before the target index
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1

        # Step 4: Validate index
        if not current:
            raise IndexError("Index out of bounds")

        # Step 5: Rewire pointers to insert the new node
        new_node.next = current.next
        current.next = new_node

    # -------------------------------
    # Display method: print all nodes in the list
    # -------------------------------
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# -------------------------------
# Example usage
# -------------------------------
ll = LinkedList()
ll.append(5)
ll.append(10)
ll.append(15)
ll.append(20)

print("Before insertion:")
ll.display()

ll.insert_at(2, 30)  # Insert 30 at index 2 (between 10 and 15)

print("After insertion:")
ll.display()
