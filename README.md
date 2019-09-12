# Daily-Coding-Problems
Python 3 coding solutions to the daily coding problems from https://dailyinterviewpro.com

---

#### Daily Problem 001

Asked by Facebook:

You are given a list of numbers, and a target number k. Return whether or not
there are two numbers in the list that add up to k.

Example:
Given `[4, 7, 1 , -3, 2]` and `k = 5`,
return `True` since `4 + 1 = 5`.

[starting code]
```
def two_sum(list, k):
    # Fill this in.

print two_sum([4,7,1,-3,2], 5)
# True
```

Bonus: Try to do it in a single pass of the list.

[Solution](code-solutions/Solution_001.py)

---

#### Daily Problem 002

Asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

[starting code]
```
class Solution:
    def lengthOfLongestSubstring(self, s):
        # Fill this in.

print(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxxabcdefghijk"))
# 12
print(Solution().lengthOfLongestSubstring("abcdcabef"))
# 6
```

Can you find a solution in linear time?

[Solution](code-solutions/Solution_002.py)

---

#### Daily Problem 003

Asked by Twitter:

You are given the root of a binary tree. Invert the binary tree in place. That is, all left children should become right children, and all right children should become left children.

Example:

     a
   /   \
  b     c
 / \   /
d   e f


The inverted version of this tree is as follows:

   a
 /   \
c     b
 \   / \
  f e   d


Here is the function signature:

```
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def preorder(self):
        print self.value,
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()

def invert(node):
    # Fill this in.

root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print "\n"
invert(root)
root.preorder()
# a c f b e d
```

[Solution](code-solutions/Solution_003.py)

---

#### Daily Problem 004

Asked by Apple:

Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

Here is the definition of a node for the tree.

```
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    # Fill this in.

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print findCeilingFloor(root, 5)
# (4, 6)
```

[Solution](code-solutions/Solution_004.py)

---

#### Daily Problem 005

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

[Solution](code-solutions/Solution_005.py)

---