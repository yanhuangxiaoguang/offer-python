# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

s = Solution()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
s.push(4)
s.push(5)
print(s.pop())
print(s.pop())
s.push(6)
print(s.pop())
print(s.pop())
print(s.pop())