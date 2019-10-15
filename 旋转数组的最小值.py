# -*- coding: utf-8 -*-
"""
题目描述：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，
输出旋转数组的最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

解题思路(胡说)：由题可得，非递减排序即递增排序，求最小值，python 有很多方法，且有内置函数min（），可直接都得到最小值。
不使用内置函数，
方法一：直接暴力比较，从头开始，当第i+1 个数比第i 个数小，就返回第i+1个数（旋转数组的特性）
方法二：利用折半查找的原理。数组的首项肯定大于或等于尾项（无翻转的例外），和中间项比较，如果中间项比首项大，最小数在后
半段，如果中间项比首项小，则最小数在前半段，然后一直循环，当一次循环中首项小于尾项，说明最小值就是首项。但是当首项等于
尾项等于中间项，只能在这个区域顺序查找（就一个折半查找的变形，就不写了）。

"""


class Solution:

    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        for i in range(len(rotateArray)-1):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]


'''用例'''
array0 = []
array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 1, 2]
array3 = [1, 1, 0, 1, 1]
array4 = [1, 1, 1, 1, 1]
array5 = [1]
array6 = [1, 0, 1, 1, 1]
num_array = 7

'''测试'''
s = Solution()
for i in range(num_array):
    array_name = 'array' + str(i)
    print(s.minNumberInRotateArray(locals()[array_name]))


