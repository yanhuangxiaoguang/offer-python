# -*- coding: utf-8 -*-
"""
题目描述：输入一个链表，输出该链表中倒数第k个结点。

背景知识：必须知道，链表的结构，这儿就不再赘述，需要的随便找本数据结构的书，都行。

解题思路(胡说)：本题主要考察代码的鲁棒性，注意判断链表为空，k为负或者k大于链表长度的情况。
设置两个指针A，，开始的时候，指针A，B都指向头节点，然后B向后移动k-1个结点。然后两个指针再一起移动，直到指针B所指向的
节点的next 为None,就返回A指针。

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k <= 0:
            return None
        a_node = head
        b_node = head
        for _ in range(k-1):
            if b_node.next:
                b_node = b_node.next
            else:
                return None
        while b_node.next:
            a_node = a_node.next
            b_node = b_node.next
        return a_node


'''用例'''
data_0 = [1, 2, 3, 4, 5]
k_list = [1, 2, 5, 6, 0]
'''构建单链表'''
head_node = ListNode(1)
now_node = head_node
for i in range(1, len(data_0)):
    tmp_node = ListNode(data_0[i])
    now_node.next = tmp_node
    now_node = now_node.next

'''测试'''
s = Solution()
for i in range(len(k_list)):
    try:
        print(s.FindKthToTail(head_node, k_list[i]).val)
    except:
        print(None)