# -*- coding: utf-8 -*-
"""
题目描述：请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。

解题思路(胡说)：这题就有多种方法实现，方法一：python 的内置函数replace()。方法二：创建一个空串，遍历字符串，如果不是空格，
就正常复制，如果是就在新串上填充‘20%’，填充的方式可以是字符串拼接，也可以是append，都差不多。
方法三：同样遍历，然后通过替代并插入的方式。
注意不要犯：
if s[i] == " ":
    s[i] = '%20'
这种错误，错误原因，将只有一个字符位，赋值了三个字符
"""

class Solution:
    """"""

    '''方法一， 利用replace()'''
    def replaceSpace0(self, s):
        if type(s) != str:
            return
        return s.replace(' ', '%20')

    '''方法二：创建新串'''
    def replaceSpace1(self, s):
        if type(s) != str:
            return
        tmp_s = ''
        for i, e in enumerate(s):
            if e != ' ':
                tmp_s += e
            else:
                tmp_s += '%20'
        return tmp_s

    '''方法三：在原串上切片拼接，或者用insert也是类似的'''
    def replaceSpace2(self, s):
        if type(s) != str:
            return
        new_s = s
        count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                new_s = new_s[:i+count*2] + '%20' + s[i+1:]
                count += 1
        return new_s

'''用例'''
case_0 = 'We%20Are%20Happy'
case_1 = ' W '
case_2 = '   '
case_3 = ''
case_4 = []

'''用例的个数'''
case_num = 5

'''方法个数'''
method_num = 3

'''测试'''
solution = Solution()
for i in range(case_num):
    for j in range(method_num):
        s_str = 'case_' + str(i)
        # print(solution.replaceSpace0(locals()[s_str]))
        print(eval('solution.replaceSpace%d(locals()[s_str])' % j))
