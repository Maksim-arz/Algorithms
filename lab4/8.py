class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue из пустой очереди")
        return self._data.pop(0)

    def front(self):
        if self.isEmpty():
            raise IndexError("front пустой очереди")
        return self._data[0]

    def isEmpty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


def generate_binary(n):
    result = []
    q = Queue()
    q.enqueue("1")
    for _ in range(n):
        current = q.dequeue()
        result.append(current)
        q.enqueue(current + "0")
        q.enqueue(current + "1")
    return result


print("N = 5")
print("Output:")
for b in generate_binary(5):
    print(b)

n = int(input("\nВведите N: "))
for b in generate_binary(n):
    print(b)
