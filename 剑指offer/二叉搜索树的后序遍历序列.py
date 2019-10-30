# -*- coding: utf-8 -*-
"""
题目描述：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的
任意两个数字都互不相同。

背景知识：二叉查找树（英语：Binary Search Tree），也称为二叉搜索树、有序二叉树（ordered binary tree）或排序二叉树
（sorted binary tree），是指一棵空树或者具有下列性质的二叉树：
1.若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
2.若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
3.任意节点的左、右子树也分别为二叉查找树；
4.没有键值相等的节点。
后序遍历:遍历二叉树的方式是，先左后右再根

解题思路(胡说)：由于后续遍历，所以序列sequence的最后一位root，必定是根元素，然后循环遍历sequence，找到第一个比root大的
数 记其在第index位置上，由二叉搜索树的性质加后续遍历，index 前面应该为root的左子树，后面为root的右子树，右子树应该满足
所有元数都大于root，否者return False。然后再分别判断左子树和右子树是否满足条件，记住右子树要把最后的根节点去掉[index:-1]
如果是递增序列或递减顺序，可以提前return True，这是特殊情况，单链树结构。记住：不能是根节点root满足是最大值或最小值就
return True.这种说明它只有左子树，或者右子树，不能代表它的左子树或者右子树满足二叉搜索树的性质（珠玉中的瑕疵）。要判断
sequence是否递增递减也要循环遍历sequence，故这种情况没有必要单独考虑。
还有当树只有两个节点的时候，可以提前return True，应为两个节点，不论是 大 、小 还是 小、 大序列，都满足二叉搜索树。减少
不必要的判断。

"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        root = sequence[-1]
        lenth = len(sequence)
        if lenth < 3:
            return True
        index = 0
        for i in range(lenth):
            index = i
            if sequence[i] > root:
                break
        if min(sequence[index:]) < root:
            return False
        left = True
        if index > 2:
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        if len(sequence[index:]) > 2:
            right = self.VerifySquenceOfBST(sequence[index:-1])
        return left and right


'''用例'''
sequence0 = [5, 7, 6, 9, 11, 10, 8]
sequence1 = [4, 6, 7, 5]
sequence2 = [1, 2, 3, 4, 5]
sequence3 = [1, 2, 6, 3, 4, 5]
sequence4 = [1, 2, 6, 3, 4, 7]
test_num = 5
'''应该的结果
True
True
True
False
False'''

'''测试'''
s = Solution()
for i in range(test_num):
    sequence_name = 'sequence%d' % i
    print(s.VerifySquenceOfBST(locals()[sequence_name]))
