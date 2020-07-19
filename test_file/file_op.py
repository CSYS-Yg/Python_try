# 文件的基本操作

# # 1.将小说的主要人物记录在文件中
# # 参数参考地址  https://www.runoob.com/python/python-func-open.html
# file1 = open('test_file/name.txt', 'w')  # 读取文件赋值给 file 1
# file1.write('诸葛亮')  # 写入操作
# file1.close()  # 操作完成 类似保存 关闭文件

# # 2.读取文件类容
# # 不加参数 默认为只读
# file2 = open('test_file/name.txt')  # 打开文件
# print(file2.read())  # 读取文件内容,并打印
# file2.close()  # 操作完成关闭文件

# 3.对已有文件进行内容增加
file3 = open('test_file/name.txt', 'a')  # 打开文件
file3.write(' 刘备')  # 原有内容后增加内容
file3.close()
