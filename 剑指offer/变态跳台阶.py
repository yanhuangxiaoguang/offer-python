# -*- coding: utf-8 -*-
"""
题目描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

背景知识：循环和递归

解题思路(胡说)：本题和斐波那契数列数列，以及跳台阶都是类似的，主要考虑数学建模能力，或者归纳总结的能力。
台阶数：1   2   3   4   5
跳法数：1   2   4   8   ？
由此观察跳法数等于 2 的（n-1）次方。本题也可以用排列组合的知识解决（略）

"""

class Solution:
    def jumpFloorII(self, number):
        if number == 0:
            return 0
        return 2 ** (number-1)


'''测试'''
s = Solution()
for i in range(5):
    print(s.jumpFloorII(i))
