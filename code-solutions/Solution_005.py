class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxl = []
        self.maxLen = 0
        self.stkLen = 0

    def push(self, val):
        self.stack.append(val)
        self.stkLen += 1
        if(self.maxLen == 0 or val > self.stack[self.maxl[self.maxLen - 1]]):
            self.maxl.append(self.stkLen - 1)
            self.maxLen += 1

    def pop(self):
        if(not self.stkLen):
            return None
        popVal = self.stack.pop()
        self.stkLen -= 1
        if(self.stkLen == self.maxl[self.maxLen - 1]):
            self.maxl.pop()
            self.maxLen -= 1
        return popVal

    def max(self):
        if(not self.maxLen):
            return None
        return self.stack[self.maxl[self.maxLen - 1]]



if(__name__ == "__main__"):
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print(s.max())
    # 3
    s.pop()
    s.pop()
    print(s.max())
    # 2
    s.pop()
    print(s.max())
    # 1
    s.pop()
    print(s.max())
    # None
    print(s.pop())
    # None