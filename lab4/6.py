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


    def __str__(self):
        return "front -> " + ", ".join(map(str, self._data)) + " <- back"


q = Queue()
print("Очередь пуста?", q.isEmpty())

for name in ("A", "B", "C", "D", "E"):
    q.enqueue(name)
    print(f"enqueue({name}) -> size = {q.size()}, front = {q.front()}")

print(q)
print("Очередь пуста?", q.isEmpty())

print("\nFIFO: первым пришёл - первым вышел")
while not q.isEmpty():
    print(f"dequeue() -> {q.dequeue()}, осталось: {q.size()}")

print("Очередь пуста?", q.isEmpty())

try:
    q.dequeue()
except IndexError as e:
    print("Ошибка:", e)
