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
        new_node = Node(data)   # Create a new node with the given data

        # Case 1: If the list is empty, new node becomes the head
        if not self.head:
            self.head = new_node
            return

        # Case 2: Otherwise, traverse to the last node
        last = self.head
        while last.next:        # Keep moving until you reach the node with next = None
            last = last.next

        # Link the last node to the new node
        last.next = new_node

    # -------------------------------
    # Display method: print all nodes in the list
    # -------------------------------
    def display(self):
        current = self.head     # Start from the head node
        while current:          # Traverse until current becomes None
            print(current.data, end=" -> ")  # Print the node's value
            current = current.next           # Move to the next node
        print("None")           # End of the list marker


# -------------------------------
# Example usage
# -------------------------------
ll = LinkedList()       # Create an empty linked list
ll.append(10)           # Add node with value 10
ll.append(20)           # Add node with value 20
ll.append(30)           # Add node with value 30

ll.display()            # Output: 10 -> 20 -> 30 -> None
