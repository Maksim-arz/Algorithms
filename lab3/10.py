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

    def find_min(self):
        if self.head is None:
            return None
        min_val = self.head.value
        current = self.head.next
        while current:
            if current.value < min_val:
                min_val = current.value
            current = current.next
        return min_val


ll = LinkedList()
for value in [25, 8, 17, 3, 42]:
    ll.insert_at_end(value)

print(f"Minimum = {ll.find_min()}")