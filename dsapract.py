
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    # Delete a node at a given position (0-based)
    def delete(self, pos):
        if self.head is None or pos < 0:
            print("Invalid position")
            return

        if pos == 0:
            self.head = self.head.next
            return

        temp = self.head
        for _ in range(pos - 1):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next


# Create linked list
List = LinkedList()

List.append(Node(1))
List.append(Node(2))
List.append(Node(3))
List.append(Node(4))
List.append(Node(5))
List.append(Node(6))
List.append(Node(7))

print("Elements:")
List.display()

List.insert(Node(8), 3)
print("After Insertion:")
List.display()

List.delete(0)
print("After Deletion:")
List.display()
