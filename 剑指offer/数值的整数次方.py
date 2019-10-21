# -*- coding: utf-8 -*-
"""
题目描述：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。保证base和exponent不同时为0

背景知识：这道题python完成不太需要背景知识

解题思路(胡说)：通过幂运算符 ** ，或者循环计算，不过要考虑 底数为0 和指数为0 ，为负的情况

"""


class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if base == 0:
            return 0
        return base ** exponent

    def Power2(self, base, exponent):
        if exponent == 0:
            return 1
        if base == 0:
            return 0
        tmp_base = 1
        if exponent < 0:
            for i in range(-exponent):
                tmp_base *= base
            return 1/tmp_base
        else:
            for i in range(exponent):
                tmp_base *= base
            return tmp_base
    '''珠玉中也有bug'''
    def Power3(self, base, exponent):
        if exponent == 0:
            return 1
        if base == 0:
            return 0
        if exponent == -1:
            return 1 / base
        result = self.Power(base, exponent >> 1)
        result *= result
        if (exponent & 0x1) == 1:
            result *= base
        return result
# write code here


'''用例'''
base_list = [-2.0, 0, 1, 2.0, 5]
exponent_list = [-2, -1, 0, 1, 2, -10]

'''测试'''
s = Solution()
for i in range(len(base_list)):
    for j in range(len(exponent_list)):
        print(s.Power(base_list[i], exponent_list[j]))
        print(s.Power2(base_list[i], exponent_list[j]))
        print(s.Power3(base_list[i], exponent_list[j]))

