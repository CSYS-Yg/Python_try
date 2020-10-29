# 新建 epub 项目结构

import os

path = "F:\EpubText\/"  # 指定存取目录

epubName = "kexuezhandouzhinan"  # 设置书名，最好为英文

fixedNmae = [
    "/META-INF/", "/OEBPS/", "/OEBPS/content/", "/OEBPS/css/", "/OEBPS/img/"
]

container = """
<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0"
    xmlns="urn:oasis:names:tc:opendocument:
    xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>
"""

mimetype = """
application/epub+zip
"""


# 新建结构文件夹
def newFolder():
    for i in fixedNmae:
        newPath = path + epubName + i
        if not os.path.exists(os.path.split(newPath)[0]):
            # 目录不存在创建，makedirs可以创建多级目录
            os.makedirs(os.path.split(newPath)[0])
    newMimetype()


def newMimetype():
    newPath = path + epubName + fixedNmae[0] + "container.xml"
    if not os.path.exists(os.path.split(newPath)[0]):
        os.makedirs(os.path.split(newPath)[0])
    with open(newPath, 'wb') as fileName:
        fileName.write(container.encode())
        fileName.close()
    newPath = path + "mimetype"
    if not os.path.exists(os.path.split(newPath)[0]):
        os.makedirs(os.path.split(newPath)[0])
    with open(newPath, 'wb') as fileName:
        fileName.write(mimetype.encode())
        fileName.close()
