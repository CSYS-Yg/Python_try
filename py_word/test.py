# 读取docx中的文本代码示例

# import docx
# # 获取文档对象
# file = docx.Document("test.docx")
# print("段落数:" + str(len(file.paragraphs)))

# # # 输出段落编号及段落内容
# for i in range(5):
#     p = file.paragraphs[i]
#     if len(p.text) > 0:
#         print("第" + str(i) + "段的内容是：" + p.text)
#         print(p.runs[0].add_picture)
#         print(dir(p.runs[0].add_tab))
#         print(p.runs[0].font.color.rgb)
#         print(p.runs[0].style)
#         print(p.runs[0].font.size.pt)

# run 下枚举的属性
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__','__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
#  '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__','__new__', '__reduce__', '__reduce_ex__', '__repr__',
#   '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__','_element', '_parent', '_r',
#   'add_break', 'add_picture', 'add_tab', 'add_text', 'bold', 'clear','element', 'font', 'italic', 'part', 'style', 'text', 'underline']

from pydocx import PyDocX

html = PyDocX.to_html("test.docx")

f = open("test.html", 'w', encoding="utf-8")

f.write(html)

f.close()
