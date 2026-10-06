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


class Task:
    def __init__(self, task_id, student, pages):
        self.task_id = task_id
        self.student = student
        self.pages = pages


printer_queue = Queue()
printer_queue.enqueue(Task(1, "Алия", 5))
printer_queue.enqueue(Task(2, "Данияр", 2))
printer_queue.enqueue(Task(3, "Мадина", 8))
printer_queue.enqueue(Task(4, "Ержан", 3))

total_pages = 0
order = 0
print("Порядок обработки задач:")
while not printer_queue.isEmpty():
    task = printer_queue.dequeue()
    order += 1
    total_pages += task.pages
    print(f"{order}. Task {task.task_id} | {task.student} | {task.pages} стр. | всего напечатано: {total_pages}")

print(f"\nИтого напечатано страниц: {total_pages}")
