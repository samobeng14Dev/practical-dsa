# -----------------------------------------
# Node: a single element in the linked list
# -----------------------------------------
class Node:
    def __init__(self, data):
        self.data = data   # Store node's value
        self.next = None   # Pointer to the next node (None if no next)


# -----------------------------------------
# LinkedList: manages a chain of Node objects
# -----------------------------------------
class LinkedList:
    def __init__(self):
        self.head = None   # Points to the first node in the list

    # -----------------------------------------
    # append(data): add a new node at the end
    # -----------------------------------------
    def append(self, data):
        new_node = Node(data)     # Create the new tail node
        if not self.head:         # Empty list: new_node becomes the head
            self.head = new_node
            return

        # Non-empty list: traverse to the current tail
        last = self.head
        while last.next:          # Move forward until last.next is None (tail found)
            last = last.next

        last.next = new_node      # Link old tail to new tail

    # -----------------------------------------
    # delete_at(index): remove the node at position `index`
    # -----------------------------------------
    def delete_at(self, index):
        # Edge case: cannot delete from an empty list
        if not self.head:
            raise IndexError("List is empty")

        # Special case: delete the head (index 0)
        if index == 0:
            # Move head forward; old head becomes unreachable
            self.head = self.head.next
            return

        # Traverse to the node just BEFORE the one to delete
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1

        # Validate: if current is None (short list) OR the target node doesn't exist
        # (i.e., current.next is None), the index is out of bounds
        if not current or not current.next:
            raise IndexError("Index out of bounds")

        # Skip over the target node by rewiring pointers:
        # Before: current -> [target] -> [after]
        # After:  current -----------------> [after]
        current.next = current.next.next

    # -----------------------------------------
    # display(): print the list as "a -> b -> c -> None"
    # -----------------------------------------
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# -----------------------------------------
# Example usage
# -----------------------------------------
ll = LinkedList()
ll.append(5)
ll.append(10)
ll.append(15)
ll.append(20)

print("Before deletion:")
ll.display()

ll.delete_at(2)  # Delete node at index 2 (value 15)

print("After deletion:")
ll.display()
