class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)

        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def insert_at(self,index,data):
        new_node=Node(data)
        if index==0:
            self.head=new_node
            return
        count=0
        current=self.head
        while count and current < index-1:
            current=current.next
            count +=1

            if not index:
                raise IndexError("Index out of bound")

        # connects the new node to the rest of the chain.
        new_node.next=current.next
        # This is the actual insertion step: the new node is placed right after current.
        current.next=new_node

    def display(self):
        current =self.head
        while current:
            print(current.data, end=' -> ')
            current=current.next
        print('None')

ll=LinkedList()
ll.append(5)
ll.append(10)
ll.append(15)
ll.append(20)
print("Before insertion:")
ll.display()

ll.insert_at(2, 30)  # Insert 30 at index 2 (between 10 and 15)

print("After insertion:")
ll.display()


  # Insert_at method: insert a node at a specific index
 # Step 2: Handle insertion at the head
# Step 3: Traverse to the node just before the target index
 # Step 4: Validate index
 # Step 5: Rewire pointers to insert the new node