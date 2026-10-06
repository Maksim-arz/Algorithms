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


    def __str__(self):
        return "Stack(" + ", ".join(map(str, self._data)) + ") <- вершина"


s = Stack()
print("Стек пуст?", s.isEmpty())

for i in range(1, 13):
    s.push(i * 10)
    print(f"push({i * 10}) -> size = {s.size()}, peek = {s.peek()}")

print(s)
print("Стек пуст?", s.isEmpty())

print("\nИзвлечение элементов:")
while not s.isEmpty():
    print(f"pop() -> {s.pop()}, осталось: {s.size()}")

print("Стек пуст?", s.isEmpty())

try:
    s.pop()
except IndexError as e:
    print("Ошибка:", e)
