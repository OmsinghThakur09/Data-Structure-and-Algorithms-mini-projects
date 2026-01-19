from os import error


class Stack:
    def __init__(self):
        self.container = []

    def pop(self):
        if len(self.container) == 0:
            raise error('cannot pop from empty stack!')
        else:
            return self.container.pop()

    def push(self, val):
        self.container.append(val)

    def is_empty(self):
        if len(self.container) == 0:
            return True
        else:
            return False

    def peek(self):
        if len(self.container) == 0:
            raise error('stack is empty!')
        else:
            return self.container[-1]

    def size(self):
        return len(self.container)

    def clear(self):
        self.container.clear()
        