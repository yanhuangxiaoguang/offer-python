# -*- coding: utf-8 -*-
"""
题目描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
（先后次序不同算不同的结果）。

背景知识：需要循环和递归的知识

解题思路(胡说)：如果没有清楚的思路，可以把前几个写出来观察规律
台阶数：1   2   3   4   5
跳法数：1   2   3   5   8
由此观察也是以1 开始的斐波那契数列数列，实现就比较简单了。如果要细究原理：设n-1个台阶，有a种跳法，当有n个台阶，
我们可以在a种跳法的基础上再跳一步，如果a中跳法中，最有一跳为一步的有m 种，我们也可以把m 种跳一步的，变成跳两步，
故n 个台阶共有 a + m 种跳法，顺推n +1 个台阶共有 a + m + a 即 n-1 加上n 个台阶的方法符合斐波那契数列特性

"""


class Solution:
    def jumpFloor(self, number):
        if number == 0:
            return 0
        fib_array = [1, 2]
        if number >= 3:
            for i in range(3, number+1):
                fib_array[(i-1) % 2] = fib_array[0] + fib_array[1]
        return fib_array[(number-1) % 2]


n = 19
'''测试'''
s = Solution()
for i in range(n):
    print(s.jumpFloor(i))


