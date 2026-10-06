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


class TextEditor:
    def __init__(self):
        self._undo = Stack()
        self._redo = Stack()

    def write(self, text):
        self._undo.push(text)
        self._redo = Stack()

    def undo(self):
        if self._undo.isEmpty():
            print("Нечего отменять")
            return
        self._redo.push(self._undo.pop())

    def redo(self):
        if self._redo.isEmpty():
            print("Нечего повторять")
            return
        self._undo.push(self._redo.pop())

    def showText(self):
        print("Text:", "".join(self._undo._data))


e = TextEditor()
e.write("Hello")
e.write(" World")
e.showText()

e.undo()
e.showText()

e.redo()
e.showText()

print()
e.write("!")
e.write("!!")
e.showText()
e.undo()
e.undo()
e.undo()
e.showText()
e.undo()
e.undo()
e.showText()
e.redo()
e.redo()
e.redo()
e.showText()
e.redo()
e.write("?")
e.showText()
e.redo()
