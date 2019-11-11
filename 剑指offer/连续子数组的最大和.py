# -*- coding: utf-8 -*-
"""
题目描述：HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需
要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正
数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子
序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

背景知识：

解题思路(胡说)：
方法一：暴力遍历
方法二：动态规划
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return None
        array_len = len(array)
        if array_len == 1:
            return array[0]
        max_num = array[0]
        for i in range(array_len):
            for j in range(i+1,array_len+1):
                tmp_max = sum(array[i:j])
                if tmp_max > max_num:
                    max_num = tmp_max
        return max_num

    def FindGreatestSumOfSubArray2(self, array):
        if not array:
            return 0
        max_list = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or max_list[i-1] <= 0:
                max_list[i] = array[i]
            else:
                max_list[i] = max_list[i-1] + array[i]
        return max(max_list)


'''用例'''
test0 = [6,-3,-2,7,-15,1,2,2]
test1 = [6,-3,-2,7,-15,1,2,2,4]
test2 = []
test3 = [-1]
test4 = [1,2,3,4]
'''用例的个数'''
test_num = 5
'''测试'''
s = Solution()
for i in range(test_num):
    test_name = 'test%d' % i
    print(s.FindGreatestSumOfSubArray(locals()[test_name]))
    print(s.FindGreatestSumOfSubArray2(locals()[test_name]))

