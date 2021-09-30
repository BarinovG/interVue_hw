class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def __check_isEmpty(self):
        if self.isEmpty:
            raise IndexError('list index out of range')

    # проверка стека на пустоту. Метод возвращает True или False
    @property
    def isEmpty(self):
        return self.size == 0

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, element):
        self.size += 1
        self.stack.append(element)

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    @property
    def peek(self):
        self.__check_isEmpty()
        return self.stack[-1]

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    @property
    def pop(self):
        self.__check_isEmpty()
        self.size -= 1
        return self.stack.pop()




