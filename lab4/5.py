class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop из пустого стека")
        return self._data.pop()

    def isEmpty(self):
        return len(self._data) == 0


def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Число должно быть неотрицательным")
    if n == 0:
        return "0"

    stack = Stack()
    while n > 0:
        stack.push(n % 2)
        n //= 2

    result = ""
    while not stack.isEmpty():
        result += str(stack.pop())
    return result


for num in (25, 0, 1, 10, 255):
    print(f"Input: {num}  Output: {decimal_to_binary(num)}")

n = int(input("\nВведите целое неотрицательное число: "))
print("Двоичное:", decimal_to_binary(n))
