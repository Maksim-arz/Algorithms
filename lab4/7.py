class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop из пустого стека")
        return self._data.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek из пустого стека")
        return self._data[-1]

    def isEmpty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


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


def reverse_queue(queue):
    stack = Stack()
    while not queue.isEmpty():
        stack.push(queue.dequeue())
    while not stack.isEmpty():
        queue.enqueue(stack.pop())


def queue_to_str(queue):
    return " ".join(map(str, queue._data))


q = Queue()
for x in (10, 20, 30, 40, 50):
    q.enqueue(x)

print("Input: ", queue_to_str(q))
reverse_queue(q)
print("Output:", queue_to_str(q))

numbers = input("\nВведите числа через пробел: ").split()
q = Queue()
for x in numbers:
    q.enqueue(int(x))
reverse_queue(q)
print("Результат:", queue_to_str(q))
