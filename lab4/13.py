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


class Browser:
    def __init__(self):
        self._back = Stack()
        self._forward = Stack()
        self._current = None

    def visit(self, page):
        if self._current is not None:
            self._back.push(self._current)
        self._current = page
        self._forward = Stack()
        print(f"Visit: {page}")

    def back(self):
        if self._back.isEmpty():
            print("Back: нет предыдущей страницы")
            return
        self._forward.push(self._current)
        self._current = self._back.pop()
        print(f"Back -> {self._current}")

    def forward(self):
        if self._forward.isEmpty():
            print("Forward: нет следующей страницы")
            return
        self._back.push(self._current)
        self._current = self._forward.pop()
        print(f"Forward -> {self._current}")

    def currentPage(self):
        return self._current


b = Browser()
b.visit("Google")
b.visit("YouTube")
b.visit("GitHub")
b.back()
b.back()
b.forward()
print("Текущая страница:", b.currentPage())

b.visit("Wikipedia")
b.forward()
b.back()
b.back()
b.back()
print("Текущая страница:", b.currentPage())
