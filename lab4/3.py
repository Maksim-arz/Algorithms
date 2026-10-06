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


PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(expr):
    stack = Stack()
    for ch in expr:
        if ch in "([{":
            stack.push(ch)
        elif ch in PAIRS:
            if stack.isEmpty() or stack.pop() != PAIRS[ch]:
                return False
    return stack.isEmpty()


for expr in ("{[()]}", "{[(])}", "((()))", "(()", "())", "a + (b * [c - d])", ""):
    status = "Balanced" if is_balanced(expr) else "Not balanced"
    print(f'Input:  "{expr}"\nOutput: {status}\n')

expr = input("Введите выражение: ")
print("Balanced" if is_balanced(expr) else "Not balanced")
