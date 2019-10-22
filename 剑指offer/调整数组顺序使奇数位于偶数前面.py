# -*- coding: utf-8 -*-
"""
题目描述：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组
的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

背景知识：无

解题思路(胡说)：
方法一：新建两个数组，遍历整个数组，奇数和偶数分别放入一个list，然后再拼接两个数组就行。


"""


class Solution:
    def reOrderArray(self, array):
        if len(array) == 0:
            return []
        array_even = []
        array_odd = []
        for i, e in enumerate(array):
            if e % 2 == 1:
                array_odd.append(e)
            else:
                array_even.append(e)
        return array_odd + array_even


'''用例'''
list0 = []
list1 = [-1, 0, 1]
list2 = [-1, -2, -3, 0, 1, 2, 3]
list3 = [1, 2, 3, 4, 5, -1, -2 , -3, -4, -5]
'''用例的个数'''
test_num = 4
'''测试'''
s = Solution()
for i  in range(test_num):
    array = 'list%d' % i
    print(s.reOrderArray(locals()[array]))
