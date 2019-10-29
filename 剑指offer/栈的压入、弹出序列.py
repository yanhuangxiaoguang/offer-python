# -*- coding: utf-8 -*-
"""
题目描述：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字
均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序
列的弹出序列。（注意：这两个序列的长度是相等的）

背景知识：栈

解题思路(胡说)：

建立一个辅助栈，把push序列的数字依次压入辅助栈tmp_stack，每次压入后，比较tmp_stack的栈顶元素和pop序列的首元素是否相等，
相等的话就出栈pop序列的首元素和tmp_stack的栈顶元素，出栈后要继续比较新的tmp_stack的栈顶元素和pop序列的首元素.直到不相等
。若最后tmp_stack为空，则push序列可以对应于pop序列。
"""


class Solution:
    def IsPopOrder(self, pushV:list, popV:list):
        if not pushV and not popV:
            return
        tmp_stack = []
        for _, e in enumerate(pushV):
            tmp_stack.append(e)
            while tmp_stack and tmp_stack[-1] == popV[0]:
                tmp_stack.pop()
                popV.pop(0)
        if not popV:
            return True
        else:
            return

pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrder(pushV, popV))
print(S.IsPopOrder(pushV, popVF))

