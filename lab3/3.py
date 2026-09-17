class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        parts = []
        while current:
            parts.append(str(current.value))
            current = current.next
        parts.append("NULL")
        print(" -> ".join(parts))

ll = LinkedList()
for value in [10, 20, 30]:
    ll.insert_at_end(value)


print("Before:", end=" ")
ll.print_list()

ll.insert_at_end(40)

print("After:", end=" ")
ll.print_list()