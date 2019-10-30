# -*- coding: utf-8 -*-
"""
题目描述：输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往
下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

背景知识：二叉树的遍历

解题思路(胡说)：就是递归的思路，最后注意将等到的结果，根据长度排序就行。

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):

        def find_path(root, expectNumber):
            if not root :
                return []
            tmp_num = expectNumber - root.val
            if not root.left and not root.right:
                if tmp_num == 0:
                    return [[root.val]]
                else:
                    return []
            a = find_path(root.left, tmp_num) + find_path(root.right, tmp_num)
            return [[root.val] + i for i in a]
        tmp_result = find_path(root, expectNumber)
        tmp_result.sort(key=lambda i: len(i),reverse=True)
        return tmp_result


'''用例
    	     8
    	   /   \
    	  6    10
    	 / \   / \
    	11 10 6   5
    	           \
    	            1
输出
'''
node_0 = TreeNode(8)
node_1 = TreeNode(6)
node_2 = TreeNode(10)
node_3 = TreeNode(11)
node_4 = TreeNode(10)
node_5 = TreeNode(6)
node_6 = TreeNode(5)
node_7 = TreeNode(1)

node_0.left = node_1
node_0.right = node_2
node_1.left = node_3
node_1.right = node_4
node_2.left = node_5
node_2.right = node_6
node_6.right = node_7
'''测试'''
s = Solution()
print(s.FindPath(node_0, 24))
