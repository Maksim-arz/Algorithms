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


class QueueTwoStacks:
    def __init__(self):
        self._in = Stack()
        self._out = Stack()

    def _transfer(self):
        if self._out.isEmpty():
            while not self._in.isEmpty():
                self._out.push(self._in.pop())

    def enqueue(self, item):
        self._in.push(item)

    def dequeue(self):
        self._transfer()
        if self._out.isEmpty():
            raise IndexError("dequeue из пустой очереди")
        return self._out.pop()

    def peek(self):
        self._transfer()
        if self._out.isEmpty():
            raise IndexError("peek пустой очереди")
        return self._out.peek()

    def isEmpty(self):
        return self._in.isEmpty() and self._out.isEmpty()


q = QueueTwoStacks()
for x in (1, 2, 3):
    q.enqueue(x)
    print(f"enqueue({x})")

print("peek() ->", q.peek())
print("dequeue() ->", q.dequeue())

q.enqueue(4)
q.enqueue(5)
print("enqueue(4), enqueue(5)")

while not q.isEmpty():
    print("dequeue() ->", q.dequeue())

print("Очередь пуста?", q.isEmpty())

print()
print("Почему это FIFO:")
print("Элементы сначала попадают в стек in, где самый старый лежит на дне.")
print("При переносе в стек out порядок меняется на обратный (LIFO + LIFO = FIFO):")
print("самый старый элемент оказывается на вершине out и извлекается первым.")
print("Перенос выполняется только когда out пуст, поэтому новые элементы")
print("не могут обогнать старые: пока в out есть элементы, они старше всех в in.")
