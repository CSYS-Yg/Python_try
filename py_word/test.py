# 读取docx中的文本代码示例

import docx
# 获取文档对象
file = docx.Document("test.docx")
print("段落数:" + str(len(file.paragraphs)))

# 输出每一段的内容
for para in file.paragraphs:
    if len(para.text) > 0:
        dir(para)
        break

# # 输出段落编号及段落内容
# for i in range(len(file.paragraphs)):
#     print("第" + str(i) + "段的内容是：" + file.paragraphs[i].text)

# from pydocx import PyDocX

# html = PyDocX.to_html("test.docx")

# f = open("test.html", 'w', encoding="utf-8")

# f.write(html)

# f.close()
