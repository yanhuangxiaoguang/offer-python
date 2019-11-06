# -*- coding: utf-8 -*-
"""
题目描述：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，
只能调整树中结点指针的指向。

背景知识：二叉搜索树，双向链表（前面的题，已经提及，不知道的建议Google 或者baidu，或者看数据结构的书）

解题思路(胡说)：先判断是否为空，返回None，没有左右子树，则返回自己，如果有左子树，处理左子树（递归调用）。然后找到左子树的最大值，
最右的节点，然后将root的left 连接到最右节点，最右节点的right连接到root。（默认left指向的小的值）同理处理右子树。

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''中序遍历'''
inorder_list = []
def inorder_traversal(x: TreeNode):
    if x:
        inorder_traversal(x.left)
        # print(str(x.val) + ' ')
        inorder_list.append(x.val)
        inorder_traversal(x.right)

def print_dobuly_link(node: TreeNode):
    data_list = []
    while node:
        data_list.append(node.val)
        node = node.right
    print(data_list)


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None

        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree

        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree

        '''返回最左的节点，最小值'''
        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree



'''用例
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9  11
输出 8 6 10 5 7 9 11

5 <=> 6 <=> 7 <=> 8 <=> 9 <=> 10 <=> 11 
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
inorder_traversal(node_0)
print('二叉搜索树的中序遍历为：'+ str(inorder_list))
'''测试'''
s = Solution()
print_dobuly_link(s.Convert(node_0))

