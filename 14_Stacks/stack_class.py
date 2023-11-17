class Stack(object):
    def __init__(self):
        self.list_stack = []

    def is_empty(self):
        if not self.list_stack:
            return True
        else:
            return False

    def push(self, item):
        self.list_stack.append(item)

    def pop(self):
        self.list_stack.pop()

    def peek(self):
        if self.list_stack == []:
            return None
        else:
            return self.list_stack[-1]

    # to return a print object when printed
    def __repr__(self):
        return repr(self.list_stack)


new_stack = Stack()
print(new_stack.is_empty())
new_stack.push(4)
new_stack.peek()
print(new_stack.peek())
new_stack.push(8)
print(new_stack)
print(new_stack.peek())
print(new_stack.is_empty())
