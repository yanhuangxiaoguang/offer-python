# -*- coding: utf-8 -*-
"""
题目描述：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

背景知识：栈的基本原理。先进先出，后进后出。

解题思路(胡说)：python的list自带pop和append（push）。最小函数，可以用python自带的min求得，也可以自己写排序算法,此方法
简单，虽然也能通过测试，但实际min的时间复杂度为O（n）.
方法二：牺牲空间复杂度最求时间复杂度，多建一个（栈），存储当前最小的栈元素。当push一个数 A 时，先将A push进入data栈。
然后判断，如果A 小于栈的min值或者栈为空，则将A 再push 进min_stack 栈，否则再将栈的最小值 push进min_stack栈，pop操作的
时候将两个栈同时pop。

"""

'''方法一：min函数时间复杂度O（n）'''
class Solution:
    def __init__(self):
        self.data_list = []
    def push(self, node):
        self.data_list.append(node)
    def pop(self):
        self.data_list.pop()
    def top(self):
        return self.data_list[-1]
    def min(self):
        return min(self.data_list)

'''方法2：min函数时间复杂度O（1），增加一倍的空间复杂度'''
class Solution1:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []
    def push(self, node):
        self.data_stack.append(node)
        if not self.min_stack or self.min() > node:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min())
    def pop(self):
        self.data_stack.pop()
        self.min_stack.pop()
    def top(self):
        return self.data_stack[-1]
    def min(self):
        return self.min_stack[-1]

'''在方法二的基础上，增加代码的鲁棒性'''
class Solutionl:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []
    def push(self, node):
        self.data_stack.append(node)
        if not self.min_stack or self.min() > node:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min())
    def pop(self):
        if not self.data_stack:
            return
        self.data_stack.pop()
        self.min_stack.pop()
    def top(self):
        if not self.data_stack:
            return None
        return self.data_stack[-1]
    def min(self):
        if not self.min_stack:
            return None
        else:
            return self.min_stack[-1]


'''测试'''
s = Solution()
s.push(1)
s.push(-2)
s.push(3)
s.push(-1)
print(s.top())
s.pop()
print(s.min())

s = Solution1()
s.push(1)
s.push(-2)
s.push(3)
s.push(-1)
print(s.top())
s.pop()
print(s.min())