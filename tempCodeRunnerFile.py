# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self, values):
        for value in values:
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

    # 2. Traverse and Print
    def display(self):
        temp = self.head

        if temp is None:
            print("Linked List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert Node at Specific Position (1-based)
    def insert(self, data, position):
        new_node = Node(data)

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find Middle Node
    def find_middle(self):
        if self.head is None:
            print("Linked List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle Node:", slow.data)

    # 5. Delete Node by Value
    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            print("Node deleted")
            return

        previous = None

        while temp and temp.data != key:
            previous = temp
            temp = temp.next

        if temp is None:
            print("Node not found")
            return

        previous.next = temp.next
        print("Node deleted")

    # 6. Reverse Linked List
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # 7. Sum of Every Two Consecutive Nodes
    def consecutive_sum(self):
        temp = self.head

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next


# Main Program
ll = LinkedList()

# Create Linked List
values = list(map(int, input("Enter elements separated by spaces: ").split()))
ll.create(values)

print("\nOriginal Linked List:")
ll.display()

# Insert Node
data = int(input("\nEnter value to insert: "))
position = int(input("Enter position: "))
ll.insert(data, position)

print("After Insertion:")
ll.display()

# Find Middle
ll.find_middle()

# Delete Node
key = int(input("\nEnter value to delete: "))
ll.delete(key)

print("After Deletion:")
ll.display()

# Reverse List
ll.reverse()

print("After Reversing:")
ll.display()

# Consecutive Sum
print("\nSum of Consecutive Nodes:")
ll.consecutive_sum()