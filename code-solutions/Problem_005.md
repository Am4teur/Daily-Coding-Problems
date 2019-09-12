# Daily Problem 005

Asked by Amazon:

Implement a stack that has the following methods:

    * `push(val)`, which pushes an element onto the stack;
    * `pop()`, which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null;
    * `max()`, which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

```
class MaxStack:
    def __init__(self):
        # Fill this in.

    def push(self, val):
        # Fill this in.

    def pop(self):
        # Fill this in.

    def max(self):
        # Fill this in.

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2
```