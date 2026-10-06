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


def evaluate_postfix(expr):
    stack = Stack()
    for token in expr.split():
        if token in "+-*/" and len(token) == 1:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            else:
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                stack.push(a / b)
        else:
            stack.push(float(token))
    result = stack.pop()
    if not stack.isEmpty():
        raise ValueError("Некорректное выражение")
    return int(result) if result == int(result) else result


for expr in ("5 3 + 2 *", "2 3 4 * +", "10 2 8 * + 3 -", "100 5 / 2 /", "7 2 /"):
    print(f"Input:  {expr}\nOutput: {evaluate_postfix(expr)}\n")

expr = input("Введите постфиксное выражение: ")
print("Результат:", evaluate_postfix(expr))
