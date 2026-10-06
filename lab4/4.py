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


def remove_adjacent_duplicates(text):
    stack = Stack()
    for ch in text:
        if not stack.isEmpty() and stack.peek() == ch:
            stack.pop()
        else:
            stack.push(ch)
    result = ""
    while not stack.isEmpty():
        result = stack.pop() + result
    return result


for word in ("abbaca", "azxxzy", "aabb", "abc", ""):
    print(f'Input:  "{word}"\nOutput: "{remove_adjacent_duplicates(word)}"\n')

text = input("Введите строку: ")
print("Результат:", remove_adjacent_duplicates(text))
