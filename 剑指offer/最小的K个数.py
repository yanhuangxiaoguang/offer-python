# -*- coding: utf-8 -*-
"""
题目描述：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

背景知识：

解题思路(胡说)：这道题，用python自带的排序，就非常简单了。自己写排序算法也行，注意判断k为0和k大于输入数组长度的情况

"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput:list, k):
        if k > len(tinput) or k == 0:
            return []
        tinput.sort()
        return tinput[:k]


'''用例'''
test0 = [5,4,3,2,1]
test1 = []
test2 = [3,2]
'''用例的个数'''
num_test = 3
k = 3
'''测试'''
s = Solution()
for i in range(num_test):
    test_name = 'test%d' % i
    print(s.GetLeastNumbers_Solution(locals()[test_name], k))
