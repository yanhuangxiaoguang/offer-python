# -*- coding: utf-8 -*-
"""
题目描述：操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
背景知识：二叉树的知识

解题思路(胡说)：循环递归，遍历二叉树，交换左右子节点。注意判断节点为空，和节点为叶子节点（没有左右子节点）的结束条件
代码中以镜像定义中的数据为测试，然后实现了一个不完善的层次遍历（输出格式只简单的靠左，没有保留父节点和子节点的关系）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''不完善的层次遍历'''
level_list_n = []
def levelorder_traversal(x: TreeNode, level=0):
    if x:
        if level < len(level_list_n):
            level_list_n[level].append(x.val)
        else:
            level_list_n.append([x.val])
        level += 1
        levelorder_traversal(x.left,level)
        levelorder_traversal(x.right,level)

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root: TreeNode):
        if not root:
            return None
        if root.left or root.right:
            tmp_node = root.left
            root.left = root.right
            root.right = tmp_node
            if root.left:
                self.Mirror(root.left)
            if root.right:
                self.Mirror(root.right)
        return root


'''用例'''
node_0 = TreeNode(8)
node_1 = TreeNode(6)
node_2 = TreeNode(10)
node_3 = TreeNode(5)
node_4 = TreeNode(7)
node_5 = TreeNode(9)
node_6 = TreeNode(11)

node_0.left = node_1
node_0.right = node_2
node_1.left = node_3
node_1.right = node_4
node_2.left = node_5
node_2.right = node_6

'''测试'''
s = Solution()
root = s.Mirror(node_0)
levelorder_traversal(root)
level_list = []
for i, e in enumerate(level_list_n):
    level_list += e
    '''不完善的层次遍历,输出格式是偏左的'''
    print(' '.join(map(str, e)))