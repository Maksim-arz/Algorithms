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

    def remove_duplicates(self):
        if self.head is None:
            return
        seen = {self.head.value}
        current = self.head
        while current.next:
            if current.next.value in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.value)
                current = current.next

    def print_list(self):
        current = self.head
        parts = []
        while current:
            parts.append(str(current.value))
            current = current.next
        parts.append("NULL")
        print(" -> ".join(parts))


ll = LinkedList()
for value in [10, 20, 10, 30, 20, 40]:
    ll.insert_at_end(value)

ll.remove_duplicates()

print("Result:", end=" ")
ll.print_list()