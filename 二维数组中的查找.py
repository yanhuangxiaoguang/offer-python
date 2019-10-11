"""
题目描述：在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数 target，判断数组中是否含有该整数。

解题思路(胡说)常见的一种错误思维，该二维数组是一个一维递增的数组变形为二位数组，如下：
A = [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
其实题目中的条件并没有说 A[i][-1] 一定要小于 A[i+1][0] 即 A[0][4] 与 A[1][0]的大小不确定。故存在这种情况：
B = [[ 0  5 10 15]
     [ 1  6 11 16]
     [ 2  7 12 17]
     [ 3  8 13 18]
     [ 4  9 14 19]]
思路一：利用折半查找的方法，可以确定在 B[i][j] < target < B[i+1][j+1] 之间的L型区域, 在用折半查找 B[i+1][0]至B[]i+1[j]
区域和B[0][j+1]至B[i][j+1]区域数。 按道理这种方法的效率应该算最快的为log n 但实现相较方法二太复杂

思路二：从二位数组的右上角 B[i][j](初始为B[0][-1]) 开始比较，
if target > B[i][j]， i += 1.
if target < B[i][j]， j -= 1.
if target = B[i][j]， return True.
当i和j 超出数组范围，则停止
"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == [] or array == [[]]:
            return False
        rows = len(array)
        cols = len(array[0])
        i = 0
        j = cols -1
        while i < rows and j >= 0:
            if target < array[i][j]:
                j -= 1
            elif target > array[i][j]:
                i += 1
            else:
                return True
        return False

'''用例'''
array0 = []
array1 = [ [ 0,  5, 10, 15],
           [ 1,  6, 11, 16],
           [ 2,  7, 12, 17],
           [ 3,  8, 13, 18],
           [ 4,  9, 14, 19] ]
array2 = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19]]
array3 = [[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
array4 = [[]]

'''用例的个数'''
array_num = 5

'''测试'''
s = Solution()
target_list = [9, 9.5, -1, 20, 4]
for m, e in enumerate(target_list):
    for k in range(array_num):
        array_name = 'array' +  str(k)
        print(s.Find(target=e, array=locals()[array_name]))
