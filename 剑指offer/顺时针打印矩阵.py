# -*- coding: utf-8 -*-
"""
题目描述：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 
10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
1   2  3  4
5   6  7  8
9  10 11 12
13 14 15 16

解题思路(胡说)：可以用now_direction来表示当前打印的方向, 并把已经打印的位置置为None，先判断是否到达边界（超出矩阵范围或
者已经被打印过了），如果到达边界就，变向（右，下，左，上的顺序循环），并同时改变角标。代码还可通过实现switch/case优化。
有点懒，感兴趣的自己去实现吧
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        data_list = []
        row_n = len(matrix)
        col_n = len(matrix[0])
        now_direction = 'right'
        i, j = 0, 0
        while len(data_list) < row_n * col_n:
            if matrix[i][j]:
                data_list.append(matrix[i][j])
                matrix[i][j] = None
            if now_direction == 'right':
                if j + 1 == col_n or not matrix[i][j+1]:
                    i += 1
                    now_direction = 'down'
                else:
                    j += 1
                continue
            if now_direction == 'down':
                if i + 1 == row_n or not matrix[i+1][j]:
                    j -= 1
                    now_direction = 'left'
                else:
                    i += 1
                continue
            if now_direction == 'left':
                if j == 0 or not matrix[i][j-1]:
                    i -= 1
                    now_direction = 'up'
                else:
                    j -= 1
                continue
            if now_direction == 'up':
                if i == 0 or not matrix[i-1][j]:
                    j += 1
                    now_direction = 'right'
                else:
                    i -= 1
                continue
        return data_list


'''用例'''
matrix0 = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix1 = [[1],[2],[3],[4],[5]]
matrix2 = [[1,2],[3,4],[5,6],[7,8],[9,10]]

'''用例的个数'''
test_num = 3

'''测试'''
s = Solution()
# print(s.printMatrix(matrix0))
# print(s.printMatrix(matrix1))
# print(s.printMatrix(matrix2))
for i in range(test_num):
    matrix_name = 'matrix%d' % i
    print(s.printMatrix(locals()[matrix_name]))
