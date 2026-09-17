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

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


ll = LinkedList()
for value in [10, 20, 30, 40]:
    ll.insert_at_end(value)

print(f"Length = {ll.get_length()}")