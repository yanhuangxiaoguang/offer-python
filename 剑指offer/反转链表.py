# -*- coding: utf-8 -*-
"""
题目描述：输入一个链表，反转链表后，输出新链表的表头。

背景知识：链表，如果顺序做题，肯定就知道链表结构

解题思路(胡说)：

方法一：创建一个空节点q_head，然后顺序遍历原链表pHead，根据当前值域生成新的节点tmp_node，然后使用头插法,将q_head插入
tmp_node的next域，然后q_head向前移，q_head=tmp_node.pHead向后移，循环直至为空
方法二：同样创建一个空节点，然后顺序遍历原链表，然后使用头插法，需要注意的是，要多用一个节点，指向当前节点的
.next域，防止，插入时丢失后续节点。
"""

'''链表值域打印函数'''
def print_node(head):
    list_val = []
    while head:
        list_val.append(head.val)
        head = head.next
    print(list_val)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead:ListNode):
        tmp_head = pHead
        q_head = None
        while tmp_head:
            tmp_node = ListNode(tmp_head.val)
            tmp_node.next = q_head
            q_head = tmp_node
            tmp_head = tmp_head.next
        return q_head


    def ReverseList1(self, pHead:ListNode):
        tmp_head = pHead
        next_head = pHead.next
        q_head = None
        while tmp_head:
            tmp_head.next = q_head
            q_head = tmp_head
            tmp_head = next_head
            if not tmp_head:
                return q_head
            next_head = next_head.next
        return q_head


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
print_node(s.ReverseList(head_node))
print_node(s.ReverseList1(head_node))
print_node(s.ReverseList(ListNode(0)))
print_node(s.ReverseList1(ListNode(0)))
