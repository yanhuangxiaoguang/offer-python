# offer-python
用python实现剑指offer等python面试编程题（写着玩）
珠玉（ https://github.com/Jack-Lee-Hiter/AlgorithmsByPython ） 在前，我的瓦砾就自己图个开心。
当然观摩（借鉴）了大佬的思路等，肯定有不同啦。欢迎提意见和建议
python == 3.7.2

面试题1：[二维数组中的查找](https://github.com/yanhuangxiaoguang/offer-python/blob/master/%E5%89%91%E6%8C%87offer/%E4%BA%8C%E7%BB%B4%E6%95%B0%E7%BB%84%E4%B8%AD%E7%9A%84%E6%9F%A5%E6%89%BE.py)
从二位数组的右上角 B[i][j](初始为B[0][-1]) 开始比较，
if target > B[i][j]， i += 1.
if target < B[i][j]， j -= 1.
if target = B[i][j]， return True.
当i和j 超出数组范围，则停止

面试题1：[替换空格](https://github.com/yanhuangxiaoguang/offer-python/blob/master/%E5%89%91%E6%8C%87offer/%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC.py)