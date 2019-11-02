# -*- coding: utf-8 -*-
"""
题目描述：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

背景知识：链表

解题思路(胡说)：这道题想不明白的，建议画图。
第一步：先遍历链，#复制原始链表的每个结点（只复制lable和next）, 将复制的结点链接在其原始结点的后面： 
原始链表的next域为 a b c d :复制节点为 A B C D ,插入后的节点a A b B c C d D
第二步：遍历链，复制节点的random指向，例如：如果原链中 a.random = c , 令 a.next.random = c.next即 A.random = C  
第三步：拆分链，将a A b B c C d D，查分成 a b c d 和A B C D 。具体的大概是:
a.next = A.next
A.next = A.next.next
然后后移
a = a.next( a 变成 b)
A = A.next（A 变成 B）

"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None

        '''复制节点，并将新的节点插入原节点后面'''
        p_node = pHead
        while p_node:
            clone_node =  RandomListNode(p_node.label)
            clone_node.next = p_node.next
            p_node.next = clone_node
            p_node = clone_node.next
        '''复制random,将原链节点的next节点的random赋值为原链被指向的next节点。'''
        p_node = pHead
        while p_node:
            clone_node = p_node.next
            if p_node.random:
                clone_node.random = p_node.random.next
            p_node = clone_node.next
        '''拆分链'''
        p_node = pHead
        clone_head = clone_node = pHead.next
        p_node.next = clone_node.next
        p_node =  p_node.next
        while p_node:
            clone_node.next = p_node.next
            clone_node = clone_node.next
            p_node.next = clone_node.next
            p_node = p_node.next
        return clone_head




'''用例'''

node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3
node2.random = node1

'''测试'''
s = Solution()


S = Solution()
clonedNode = S.Clone(node1)
tmp_node = node1
tmp_clone_node = clonedNode
while tmp_node:
    print('now_node address is same:%s' % (tmp_node == tmp_clone_node) )
    print('now_node label is equal:%s' % (tmp_node.label == tmp_clone_node.label))
    print('now_node next is same:%s' % (tmp_node.next == tmp_clone_node.next))
    print('now_node random is same:%s' % (tmp_node.random == tmp_clone_node.random))
    tmp_node = tmp_node.next
    tmp_clone_node = tmp_clone_node.next
'''注：正常应该只有label 为True， 但尾节点next和label为空，故相等'''