PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}


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


def tokenize(expr):
    tokens, current = [], ""
    for ch in expr:
        if ch.isalnum() or ch == ".":
            current += ch
        else:
            if current:
                tokens.append(current)
                current = ""
            if ch in PRECEDENCE or ch in "()":
                tokens.append(ch)
            elif not ch.isspace():
                raise ValueError(f"Недопустимый символ: {ch!r}")
    if current:
        tokens.append(current)
    return tokens


def infix_to_postfix(expr):
    output = []
    stack = Stack()

    for token in tokenize(expr):
        if token in PRECEDENCE:
            while (not stack.isEmpty() and stack.peek() != "("
                   and PRECEDENCE[stack.peek()] >= PRECEDENCE[token]):
                output.append(stack.pop())
            stack.push(token)
        elif token == "(":
            stack.push(token)
        elif token == ")":
            while not stack.isEmpty() and stack.peek() != "(":
                output.append(stack.pop())
            if stack.isEmpty():
                raise ValueError("Лишняя закрывающая скобка")
            stack.pop()
        else:
            output.append(token)

    while not stack.isEmpty():
        op = stack.pop()
        if op == "(":
            raise ValueError("Лишняя открывающая скобка")
        output.append(op)

    return " ".join(output)


tests = [
    "A + B * C",
    "(A + B) * C",
    "A - B - C",
    "A * (B + C) / D",
    "A + B * (C - D) / E",
    "((A + B) * (C - D)) / E",
    "10 + 20 * 3",
]
for t in tests:
    print(f"Input:  {t}\nOutput: {infix_to_postfix(t)}\n")

expr = input("Введите инфиксное выражение: ")
print("Постфиксная запись:", infix_to_postfix(expr))
