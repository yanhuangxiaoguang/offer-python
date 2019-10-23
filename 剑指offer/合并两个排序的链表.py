# -*- coding: utf-8 -*-
"""
题目描述：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

背景知识：还是链表的知识，

解题思路(胡说)：
方法一：两个链表A，B。分别创建一个指针p_head1, p_head2。并创建一个空链表m_head，根据p_head1, p_head2的值域中小
的值，生成新节点，插入m_head.next 移动小值的指针，然后循环比较，直到任意链表为空。然后将不为空的剩余节点插入到
m_head.next
方法二：递归版本
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
    def Merge(self, pHead1:ListNode, pHead2:ListNode):
        m_head = ListNode(-1)
        tmp_m_head = m_head
        p_head1 = pHead1
        p_head2 = pHead2
        while p_head1 and p_head2:
            if p_head1.val <= p_head2.val:
                tmp_m_head.next = ListNode(p_head1.val)
                p_head1 = p_head1.next
            else:
                tmp_m_head.next = ListNode(p_head2.val)
                p_head2 = p_head2.next
            tmp_m_head = tmp_m_head.next
        if not p_head1:
            tmp_m_head.next = p_head2
        else:
            tmp_m_head.next = p_head1
        return m_head.next


    def Merge1(self, pHead1:ListNode, pHead2:ListNode):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge1(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge1(pHead1, pHead2.next)
            return pHead2


'''用例'''
data_0 = [1, 2, 3, 4, 5]
data_1 = [-1, 1, 3, 5, 6]
'''构建单链表'''
'''注：链表1的头节点值域为0'''
p_head1 = ListNode(0)
head1 = p_head1
'''注：链表2的头节点值域为-2'''
p_head2 = ListNode(-2)
head2 = p_head2
for i in range(len(data_0)):
    tmp_node = ListNode(data_0[i])
    head1.next = tmp_node
    head1 = head1.next

    tmp_node = ListNode(data_1[i])
    head2.next = tmp_node
    head2 = head2.next

'''测试'''
s = Solution()
print_node(s.Merge(p_head1, p_head2))
print_node(s.Merge1(p_head1, p_head2))
'''其他测试样例'''
print_node(s.Merge(ListNode(0), ListNode(-1)))
print_node(s.Merge1(ListNode(0), ListNode(-1)))
print_node(s.Merge(ListNode(0), p_head2))
print_node(s.Merge1(ListNode(0), p_head2))