# 读取人物名称
# f = open('name.txt', encoding='UTF-8')
# data = f.read()  # 读取所有内容
# data0 = data.split('|')  # 通过 split 分隔
# print(data0)

# 读取 武器名称
f1 = open('weapon.txt', encoding='UTF-8')
i = 1
# 读取多行,设置筛选条件
# readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。
for line in f1.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1
