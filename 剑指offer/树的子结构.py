# -*- coding: utf-8 -*-
"""
题目描述：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

背景知识：二叉树的基本结构，有值域，左右子节点域

解题思路(胡说)：这道题，通过递归遍历就行，首先判断B的根节点和A的当前节点的值是否相等，相等就开始进行B树的完全匹配。
不相等就判断A的左右子节点是否和B的根节点是否相等。
完全匹配的时候，需要注意的是B为空的时，判断结束，B为非空的时候，A一定要非空，且值域相等，才进行子节点的匹配，
否则返回False

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1:TreeNode, pRoot2:TreeNode):
        result = False
        if pRoot2 and pRoot1:
            if pRoot2.val == pRoot1.val:
                result = self.judge_sub_tree(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def judge_sub_tree(self, root1:TreeNode, root2:TreeNode):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.judge_sub_tree(root1.left, root2.left) and self.judge_sub_tree(root1.right, root2.right)

'''用例 '''
'''Tree 1'''
node_0 = TreeNode(0)
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)

node_0.left = node_1
node_0.right = node_2
node_1.left = node_3
node_1.right = node_4
node_2.left = node_5
node_2.right = node_6
'''Tree 2'''
node_7 = TreeNode(0)
node_8 = TreeNode(2)
node_9 = TreeNode(6)
node_7.right = node_8
node_8.right = node_9

'''用例的个数'''

'''测试'''
s = Solution()
print(s.HasSubtree(node_0, node_7))
