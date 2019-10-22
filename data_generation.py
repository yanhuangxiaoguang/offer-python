import numpy as np
array1 = np.arange(20).reshape(4,5)
print(array1)
print(array1.T)

class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == []:
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

    def replaceSpace(self, s):
        new_s = s
        count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                new_s = new_s[:i+count*2] + '%20' + s[i+1:]
                count += 1
        return new_s
s = Solution()
array = np.linspace(1, 24, 24).reshape([4, 6])
array = array.T
print(array)
target = 23.5
print(s.Find(target, array))
print(s.Find(target, [[]]))
print(s.replaceSpace("   "))
print(s.replaceSpace(" asd sd"))