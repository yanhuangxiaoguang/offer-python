# -*- coding: utf-8 -*-
"""
题目描述：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法？

背景知识：空间想象能力，或者画图能力

解题思路(胡说)：这题其实和青蛙跳台阶背后的数学原理是一样的，假如有n个小矩形的时候有a 种方法，则当有n+1个小矩形的时候，
当大矩形的第n+1列 竖着放一个小矩形，则有 a 种方法，当第 n 列是竖着放的小矩形，则可以将第n列和第n+1列 横着放两个小矩形。
第 n 列是竖着放的小矩形有多少种呢 ? 同理可得 有当只有n-1个小矩形的时候的方法数。最后的 A（n+1） = A（n）+ A（n-1）
 这就是斐波那契数列。

"""


class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        fib_array = [1, 2]
        if number >=3 :
            for i in range(2, number+1):
                fib_array[i%2] = fib_array[0] + fib_array[1]
        return fib_array[(number-1)%2]


# write code here


n = 19
'''测试'''
s = Solution()
for i in range(n):
    print(s.rectCover(i))

