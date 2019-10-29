# -*- coding: utf-8 -*-
"""
题目描述：从上往下打印出二叉树的每个节点，同层节点从左至右打印。

背景知识：二叉树的层次遍历

解题思路(胡说)：
方法一：在重建二叉树中就已经实现了层次遍历，( https://github.com/yanhuangxiaoguang/offer-python/blob/master/%E5%89%91%E6%8C%87offer/%E9%87%8D%E5%BB%BA%E4%BA%8C%E5%8F%89%E6%A0%91.py )
创建一个level_list_n, level_list_n的第i个位置存放第i层节点val值的list，并引入二叉树的层数。递归的遍历整个树
（保证left在right前遍历就行）
方法二：引入一个队列, 先将根节点入队列，然后：出队列，val加入result list 中。在将其左右孩子顺序入队列，再重复出先前操作
，直至队列为空
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        level_list_n = []
        def levelorder_traversal(x, level=0):
            if x:
                if level < len(level_list_n):
                    level_list_n[level].append(x.val)
                else:
                    level_list_n.append([x.val])
                level += 1
                levelorder_traversal(x.left, level)
                levelorder_traversal(x.right, level)
        levelorder_traversal(root)
        val_list = []
        for i, e in enumerate(level_list_n):
            val_list += e
        return val_list

    def PrintFromTopToBottom1(self, root):
        queue = []
        if not root:
            return []
        result = []
        queue.append(root)
        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result


'''用例
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9  11
输出 8 6 10 5 7 9 11
'''
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
print(s.PrintFromTopToBottom(node_0))
print(s.PrintFromTopToBottom1(node_0))