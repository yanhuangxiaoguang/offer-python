# -*- coding: utf-8 -*-
"""
题目描述：输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所
有字符串abc,acb,bac,bca,cab和cba。
输入描述：输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

背景知识：排列组合的思想，字典序：Ascii码，从小到大。A-Z a-z

解题思路(胡说)：分解的思想，先把字母排序，然后顺序取一个字母，将剩下的再调用排序函数，将返回的结果和之前的拼接上，
注意要判断字符串为空为一个的情况，然后跳过相同字母。
"""


class Solution:
    def Permutation(self, ss: str):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        list_str = list(ss)
        list_str.sort()
        out_str = []
        for i in range(len(list_str)):
            if i > 0 and list_str[i] == list_str[i-1]:
                continue
            tmp_str = self.Permutation(''.join(list_str[:i])+ ''.join(list_str[i+1:]))
            for j in tmp_str:
                out_str.append(list_str[i]+j)
        return out_str



'''用例'''
string_0 = 'AcBbA'
'''用例的个数'''

'''测试'''
s = Solution()
print(s.Permutation(string_0))
