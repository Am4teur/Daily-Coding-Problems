class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if(not self.max_stack or val > self.stack[self.max_stack[-1]]):
            self.max_stack.append(len(self.stack) - 1)

    def pop(self):
        if(not self.stack):
            return None
        popVal = self.stack.pop()
        if(len(self.stack) == self.max_stack[-1]):
            self.max_stack.pop()
        return popVal

    def max(self):
        if(not self.max_stack):
            return None
        return self.stack[self.max_stack[-1]]



if(__name__ == "__main__"):
    s = MaxStack()
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(6)
    print(s.max())
    # 7
    s.pop()
    s.pop()
    print(s.max())
    # 6
    s.pop()
    print(s.max())
    # 5
    s.pop()
    print(s.max())
    # None
    print(s.pop())
    # None