# -*- coding: utf-8 -*-
"""
题目描述：输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

解题思路(胡说)：这道题如果弄懂了，什么是链表，链表的最基本结构，由值域和下一链环的地址域组成（单链表）。至于其他的什么
双向链表，循环链表，十字（交叉）链表就不在这赘述。
s首先创建一个空的list:
方法一：通过python 内置方法insert（0，data）每次在list的首部（头部，前面）插入当前值。
方法二：通过list 的 append 获得顺序的list 数据域，然后通过python的list倒序方法实现，有
list(reversed(a))
sorted(a,reverse=True)
a[: :-1] 
"""
'''单链表的数据结构'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode == None:
            return []
        tmp_list = []
        now_node = listNode
        while now_node:
            tmp_list.insert(0, now_node.val)
            now_node = now_node.next
        return tmp_list

    def python_list_reverse(self, listNode):
        if listNode == None:
            return []
        tmp_list = []
        now_node = listNode
        while now_node:
            tmp_list.append(now_node.val)
            now_node = now_node.next
        print(list(reversed(tmp_list)))
        print(sorted(tmp_list, reverse=True))
        print(tmp_list[::-1])


'''用例'''
data_0 = [1, 2, 3, 4]

'''构建单链表'''
head_node = ListNode(0)
now_node = head_node
for i, e in enumerate(data_0):
    tmp_node = ListNode(e)
    now_node.next = tmp_node
    now_node = now_node.next

'''测试'''
s = Solution()
print(s.printListFromTailToHead(head_node))
s.python_list_reverse(head_node)




