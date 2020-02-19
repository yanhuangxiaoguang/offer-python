# -*- coding: utf-8 -*-
"""
题目描述：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、
13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数
（从1 到 n 中1出现的次数）。


解题思路(胡说)：
找到其数学规律，大致把数设为 abc，其中a和c可能是0到多位，b只能为0到9的一个数，每次计算b位出现1的次数。从个位开始，引入m ，
代表第m位，可以分b=0, b = 1和 b > 1 三种情况讨论。

"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        one, m = 0, 1
        while m <= n:
            if n // m % 10 == 0:
                one += n // m // 10 * m
            elif n // m % 10 == 1:
                one += n // m // 10 * m + n % m + 1
            else:
                one += n // m // 10 * m + m
            m *= 10
        return one

    def NumberOf1Between1AndN2(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones



'''用例'''

'''用例的个数'''

'''测试'''
s = Solution()
print(s.NumberOf1Between1AndN_Solution(200))
print(s.NumberOf1Between1AndN2(200))
