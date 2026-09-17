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

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False


ll = LinkedList()
for value in [10, 25, 30, 45]:
    ll.insert_at_end(value)

print("Search 30 ->", "Found" if ll.search(30) else "Not Found")
print("Search 50 ->", "Found" if ll.search(50) else "Not Found")