# -*- coding: utf-8 -*-
"""
题目描述：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的
数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

背景知识：要实现本题，需要了解二叉树的基本概念和 先（前）序遍历、中序遍历、后续遍历、层次遍历（不常用）。
二叉树就一一个节点至多两个叶子节点的数据结构
前序遍历：根结点 ---> 左子树 ---> 右子树
中序遍历：左子树 ---> 根结点 ---> 右子树
后序遍历：左子树 ---> 右子树 ---> 根结点
层次遍历：按层次遍历
如：               1
                 /   \
               2      3 
             /       / \            
            4       5   6
             \         /    
              7       8    
前序遍历：1  2  4  7  3  5  6  8
中序遍历：4  7  2  1  5  3  8  6
后序遍历：7  4  2  5  8  6  3  1
层次遍历：1  2  3  4  5  6  7  8

解题思路(胡说)：利用二叉树前序遍历和中序遍历的特性。前序遍历的第一个值一定为根节点，对应于中序遍历中间的一个点。在中序遍历序列中，
这个点左侧的均为根的左子树，这个点右侧的均为根的右子树。这时可以利用递归，分别取前序遍历[1:i+1]和中序遍历的[:i]对应与左
子树继续上一个过程，取前序遍历[i+1:]和中序遍历[i+1]对应于右子树继续上一个过程，最终得以重建二叉树。
"""

'''牛客网给的二叉树的基本结构'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''前序遍历'''
preorder_list = []
def preorder_traversal(x: TreeNode):
    if x:
        # print(str(x.val) + ' ')
        preorder_list.append(x.val)
        preorder_traversal(x.left)
        preorder_traversal(x.right)

'''中序遍历'''
inorder_list = []
def inorder_traversal(x: TreeNode):
    if x:
        inorder_traversal(x.left)
        # print(str(x.val) + ' ')
        inorder_list.append(x.val)
        inorder_traversal(x.right)

'''后序遍历'''
postorder_list = []
def postorder_traversal(x: TreeNode):
    if x:
        postorder_traversal(x.left)
        postorder_traversal(x.right)
        # print(str(x.val) + ' ')
        postorder_list.append(x.val)

'''层次遍历'''
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
    # 返回构造的TreeNode根节点
    """直接利用前序序列和中序序列构建二叉树"""

    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None
        root_node = TreeNode(pre[0])
        i = tin.index(pre[0])
        root_node.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i])
        root_node.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root_node


pre_list = [1, 2, 4, 7, 3, 5, 6, 8]
tin_list = [4, 7, 2, 1, 5, 3, 8, 6]

'''测试'''
s = Solution()
tree = s.reConstructBinaryTree(pre_list, tin_list)
print(tree)
preorder_traversal(tree)
inorder_traversal(tree)
postorder_traversal(tree)
print(" ".join(map(str, preorder_list)))
print(" ".join(map(str, inorder_list)))
print(" ".join(map(str, postorder_list)))

levelorder_traversal(tree)
level_list = []
for i, e in enumerate(level_list_n):
    level_list += e
print(' '.join(map(str, level_list)))