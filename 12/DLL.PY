# DOUBLY LINKED LIST IMPLEMENTATION IN PYTHON
from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class doublyLinkedList:
    def __init__(self):
        self.head = None

    # Create linked list (append)
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Traverse and print the nodes
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Insert a node at a given position (0-based)
    def insert(self, new_node, pos):
        if pos < 0:
            print("Invalid position")
            return

        if pos == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    # Delete a node at a given position (0-based)
    def delete(self, pos):
        if pos < 0 or self.head is None:
            print("Invalid position")
            return

        if pos == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp is None or temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next
        if temp.next:
            temp.next.prev = temp
# Example usage
List1 = doublyLinkedList()
List1.append(Node(10))
List1.append(Node(20))
List1.append(Node(30))
List1.append(Node(40))
List1.append(Node(50))
List1.append(Node(60))

List1.display()
List1.insert(Node(25), 2)
List1.display()
