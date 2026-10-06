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


class StackTwoQueues:
    def __init__(self):
        self._q1 = Queue()
        self._q2 = Queue()

    def push(self, item):
        self._q2.enqueue(item)
        while not self._q1.isEmpty():
            self._q2.enqueue(self._q1.dequeue())
        self._q1, self._q2 = self._q2, self._q1

    def pop(self):
        if self._q1.isEmpty():
            raise IndexError("pop из пустого стека")
        return self._q1.dequeue()

    def peek(self):
        if self._q1.isEmpty():
            raise IndexError("peek пустого стека")
        return self._q1.front()

    def isEmpty(self):
        return self._q1.isEmpty()


s = StackTwoQueues()
for x in (1, 2, 3, 4):
    s.push(x)
    print(f"push({x}) -> peek = {s.peek()}")

print("pop() ->", s.pop())
s.push(5)
print("push(5) -> peek =", s.peek())

print("\nLIFO: последним пришёл - первым вышел")
while not s.isEmpty():
    print("pop() ->", s.pop())

print("Стек пуст?", s.isEmpty())
