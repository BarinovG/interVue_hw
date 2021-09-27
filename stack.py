class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def __check_not_empty(self):
        if self.is_empty:
            raise IndexError('list index out of range')

    @property
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, element):
        self.size += 1
        self.stack.append(element)

    @property
    def peek(self):
        self.__check_not_empty()
        return self.stack[-1]

    @property
    def pop(self):
        self.__check_not_empty()
        self.size -= 1
        self.stack.pop(self.size)
        return self.peek

