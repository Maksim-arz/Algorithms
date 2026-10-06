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


def reverse_string(text):
    stack = Stack()
    for ch in text:
        stack.push(ch)
    result = ""
    while not stack.isEmpty():
        result += stack.pop()
    return result


for word in ("HELLO", "Python", "stack", ""):
    print(f'Input:  "{word}"\nOutput: "{reverse_string(word)}"\n')

text = input("Введите строку: ")
print("Результат:", reverse_string(text))
