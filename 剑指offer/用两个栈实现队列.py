# -*- coding: utf-8 -*-
"""
题目描述：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

背景知识：在计算机中栈（stack）和堆（heap）大多同时出现，且在数据结构中和内存中是代表不同的东西。题目中还提到队列(queue)
数据结构中： 
栈：一种先进后出，后进先出的规则的数据结构，有进栈（push）和出栈（pop）的两个基本操作。
堆：堆就是用数组实现的二叉树，所有它没有使用父指针或者子指针。堆根据“堆属性”来排序，有最大堆和最小堆之分，“堆属性”
决定了树中节点的位置。在最大堆中，父节点的值比每一个子节点的值都要大。在最小堆中，父节点的值比每一个子节点的值都要小。
这就是所谓的“堆属性”，并且这个属性对堆中的每一个节点都成立。参考自（ https://www.jianshu.com/p/6b526aa481b1 ）
扩展 内存中:
栈：由编译器自动分配和释放，存放函数的参数值，局部变量的值等。其操作方式类似于数据结构中的栈。
堆：一般由程序员分配和释放，若程序员不释放，程序结束时可能由OS回收，

队列（queue）：队列（queue）是一种采用先进先出(FIFO)策略的抽象数据结构
解题思路(胡说)：如果不使用栈，直接用python的数组操作肯定更方便，但题目要求栈，我们还是用两个栈实现。粗鲁想法一个栈是先
进后出，而我们要实现先进先出，再加一个栈，存第一个栈pop出来的数据，两次反转，就实现队列的先进先出的性质。
细节：设队列为 queue，栈1为 stack1 ，栈2 为stack2 . 
当 queue执行push 操作，stack1 执行push操作
当 queue执行pop 操作， 如果 stack2 不为空，stack2 执行pop操作，（如果stack2没有数据，错误提示）
                       如果 stack2 为空，将stack1 所有元素 pop，并push 进 stack2. 然后stack2 执行pop
"""


class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, node):
        self.queue1.append(node)

    def pop(self):
        if not self.queue1 and not self.queue2:
            return
        if len(self.queue2) != 0:
            return self.queue2.pop()
        else:
            for i in range(len(self.queue1)):
                self.queue2.append(self.queue1.pop())
            return self.queue2.pop()

'''测试: 输出结果应为1 2 3 4 5 6'''
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
