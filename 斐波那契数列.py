# -*- coding: utf-8 -*-
"""
题目描述：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

背景知识：斐波那契数列 0 1 1 2 3 5 8 13 21 34···，第i 个数等于 第i-1 和 i-2两个数之和。
（注：有从0开始，也有从1开始的）

解题思路(胡说)：单纯的实现就比较简单了,如果是前两项，就分别等于0 和1 ，如果是后面的，就可以通过循环累加就可以。
注意一点就是别把中间的项存下来，占用空间就行。斐波那契数列还有很多变种，有时间再添加

"""


class Solution:

    def Fibonacci_old(self, n):
        fib_array = [0, 1]
        if n == 0:
            return 0
        if n == 1:
            return 1
        tmp_n = 0
        for i in range(2, n+1):
            tmp_n = fib_array[0] + fib_array[1]
            fib_array[0] = fib_array[1]
            fib_array[1] = tmp_n
        return tmp_n

    '''代码优化'''
    def Fibonacci(self, n):
        fib_array = [0, 1]
        if n >1 :
            for i in range(2, n+1):
                fib_array[i%2] = fib_array[0] + fib_array[1]
        return fib_array[n%2]


n = 19
'''测试'''
s = Solution()
for i in range(n):
    print(s.Fibonacci_old(i))
    print(s.Fibonacci(i))
