# -*- coding: utf-8 -*-
"""
题目描述：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

背景知识：数组

解题思路(胡说)：先判断输入是否为空，或者只有一个元素。然后：
方法一：利用python内置函数排序，出现次数超过一半，那排序后的中位数必定也是众数，故那中位数去遍历有数组，相等的加1，
最后再判断数量是否大于数组长度的一半。
方法二：建立数字字典，将每个数放入字典，相同的就+1,最后再判断，是否那个数出现次数大于一半。
还有好几种方法，就不列举了

"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers:list):
        if not numbers:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        numbers.sort()
        median_index = len(numbers) // 2
        mode = numbers[median_index]
        mode_num = 0
        for i in range(len(numbers)):
            if numbers[i] == mode:
                mode_num += 1
        if mode_num > median_index:
            return mode
        else:
            return 0

    def MoreThanHalfNum_Solution1(self, numbers:list):
        if not numbers:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        num_dict = dict()
        for i in range(len(numbers)):
            if numbers[i] in num_dict.keys():
                num_dict[numbers[i]] +=1
            else:
                num_dict[numbers[i]] = 1
        tmp_k, tmp_n = None, 0
        for k,v in num_dict.items():
            if v > tmp_n:
                tmp_n = v
                tmp_k = k
        if tmp_n > len(numbers) // 2:
            return tmp_k
        else:
            return 0



'''用例'''
list0 = [1,2,3,2,2,2,5,4,2]
list1 = []
list2 = [1]
list3 = [1,2,3,3,2]

'''用例的个数'''
test_num = 4
'''测试'''
s = Solution()
for i in range(test_num):
    list_name = 'list%d' % i
    print(s.MoreThanHalfNum_Solution(locals()[list_name]))
    print(s.MoreThanHalfNum_Solution1(locals()[list_name]))
