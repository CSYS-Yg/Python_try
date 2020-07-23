# 文件的基本操作

# # 1.将小说的主要人物记录在文件中
# # 参数参考地址  https://www.runoob.com/python/python-func-open.html
# # encoding='utf-8' 根据文本类型设置打开，不设置很大几率乱码
# file1 = open('./name.txt', 'w', encoding='utf-8')  # 读取文件赋值给 file 1
# file1.write('诸葛亮')  # 写入操作
# file1.close()  # 操作完成 类似保存 关闭文件

# # 2.读取文件类容
# # 不加参数 默认为只读
# file2 = open('./name.txt', encoding='utf-8')  # 打开文件
# print(file2.read())  # 读取文件内容,并打印
# file2.close()  # 操作完成关闭文件

# # 3.对已有文件进行内容增加
# file3 = open('./name.txt', 'a', encoding='utf-8')  # 打开文件
# file3.write(' 刘备')  # 原有内容后增加内容
# file3.close()

# # 4.读取一行内容
# file4 = open('./name.txt', encoding='utf-8')
# print(file4.readline())

# # 5.读取多行内容
# file5 = open('./name.txt', encoding='utf-8')
# for line in file5.readlines():
#     print(line)
#     print('=====')
# file5.close()

# 6.调试文本读取指针
file6 = open('./name.txt', encoding='UTF-8')
# .tell() 读取当前指针位置，按字节读取。一般来说，三个字节是一个字符
print('当前文件指针的位置 %s' % file6.tell())
# .read(n) 读取 n 个字符，n 为空，默认为全部；为 n 时 打印 n 个字符。会移动指针位置。
# 读取后若未关闭文本，则按读取后指针位置继续读取。
print('当前读取到了一个字符，字符的内容是 %s' % file6.read(1))  # 诸
print('当前读取到了一个字符，字符的内容是 %s' % file6.read(2))  # 葛亮
print('当前文件指针的位置 %s' % file6.tell())  # 9

# 第一个参数代表偏移位置，第二个参数  0 表示从文件开头偏移  1表示从当前位置偏移  2 从文件结尾偏移
file6.seek(3, 0)  # 从文章开头位置，偏移 3 个字节即一个字符
print('当前读取到了一个字符，字符的内容是 %s' % file6.read(1))  # 葛
