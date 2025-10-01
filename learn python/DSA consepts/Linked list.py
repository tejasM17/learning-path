# Step 1: Create a Node Class


class Node:
    def __init__(self, val):
        self.val = val  # The value stored
        self.next = None  #  Pointer to next node (starts as None)


# Step 2: Create a Linked List Class


class Linkedlist:
    def __init__(self):
        self.head = None  # First node of the list (starts empty)

    def addfirst(self, val):
        new_node = Node(val)  # Create new carriage
        new_node.next = self.head  # New node points to current head
        self.head = new_node  # New node becomes the head

    def addlast(self, val):
        new_node = Node(val)  # Create new carriage

        # If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to last node
        current = self.head

        while current.next is not None:
            current = current.next

        # Add new node at end
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.val, "->", end=" ")
            current = current.next
        print("None")


# Let's create and test!
my_list = Linkedlist()

# Add some numbers
my_list.addfirst(3)
my_list.addfirst(2)
my_list.addfirst(1)

my_list.addlast(4)

# Display the list
my_list.display()
