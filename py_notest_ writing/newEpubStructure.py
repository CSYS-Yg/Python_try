# 新建 epub 项目结构

import os

import dataList

import shutil

path = "F:\EpubText\/"  # 指定存取目录

epubName = "zhichangyuxiezuo"  # 设置书名，最好为英文

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
def newFolder(pathAdress, name):
    if pathAdress:
        path = pathAdress
    if pathAdress:
        epubName = name
    for i in fixedNmae:
        newPath = path + epubName + i
        if not os.path.exists(os.path.split(newPath)[0]):
            # 目录不存在创建，makedirs可以创建多级目录
            os.makedirs(os.path.split(newPath)[0])
    newMimetype()
    newBat()
    newCss()


def newMimetype():
    newPath = path + epubName + fixedNmae[0] + "container.xml"
    if not os.path.exists(os.path.split(newPath)[0]):
        os.makedirs(os.path.split(newPath)[0])
    with open(newPath, 'wb') as fileName:
        fileName.write(container.encode())
        fileName.close()
    newPath = path + epubName + "/mimetype"
    if not os.path.exists(os.path.split(newPath)[0]):
        os.makedirs(os.path.split(newPath)[0])
    with open(newPath, 'wb') as fileName:
        fileName.write(mimetype.encode())
        fileName.close()


# 新建 .bat 文件操作
def newBat():
    bat = """
    REM Bandizip.exe c -root:top test.zip  -r META-INF OEBPS mimetype

    SET setPath={}

    del /f /s /q %setPath%.epub

    del /f /s /q %setPath%.zip

    Bandizip.exe bc %setPath%

    ren *.zip *.epub

    """.format(epubName)
    newPath = path + "/text.bat"
    with open(newPath, 'wb') as fileName:
        fileName.write(bat.encode())
        fileName.close()


# 复制 css 文件至指定目录
def newCss():
    old_file_path = r'./css/yuguang.css'
    new_file_path = path + epubName + fixedNmae[3] + "yuguang.css"
    shutil.copyfile(old_file_path, new_file_path)


# 生成目录
def newNcx(list):
    contentBfter = """
    <?xml version="1.0" encoding="UTF-8"?>
    <ncx
    xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="bookid"/>
        <meta name="dtb:depth" content="0"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle>
        <text>职场写作与沟通：升级个人品牌, 让你10倍值钱</text>
    </docTitle>
    <!-- 菜单导航地图 -->
    <navMap>
    """
    contentAfter = """
        </navMap>
        </ncx>
    """
    newPath = path + epubName + fixedNmae[1] + "toc.ncx"
    content = ""
    for i in list:
        strNumber = dataList.getNumbering(i['number'])
        name = i["title"].split('丨')[1].replace('.note', '')
        content += """<navPoint class="chapter" id="html_%s" playOrder="1">
            <navLabel>
            <text>%s</text>
            </navLabel>
            <content src="content/test_%s.html"/>
        </navPoint>
        """ % (strNumber, name, strNumber)
    content = contentBfter + content + contentAfter
    with open(newPath, 'wb') as fileName:
        fileName.write(content.encode())
        fileName.close()


# 生成目录导航
def newOpf(list):
    contentBfter = """
    <?xml version="1.0" encoding="UTF-8"?>
    <package
    xmlns:opf="http://www.idpf.org/2007/opf" unique-identifier="bookid"
    xmlns="http://www.idpf.org/2007/opf" version="2.0">
    <metadata
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:opf="http://www.idpf.org/2007/opf"
        xmlns:dcterms="http://purl.org/dc/terms/"
        xmlns:dc="http://purl.org/dc/elements/1.1/">
        <!-- 出版物唯一标识码  -->
        <dc:contributor opf:file-as="CompanyName" opf:role="own">Epubor</dc:contributor>
        <dc:contributor opf:file-as="PersonalName" opf:role="own">Ultimate</dc:contributor>
        <dc:contributor opf:file-as="eCore" opf:role="bkp">eCore v0.9.4.611 [ http://www.epubor.com/ecore.html ]</dc:contributor>
        <dc:contributor opf:file-as="SiteURL" opf:role="own">http://www.epubor.com</dc:contributor>
        <dc:creator opf:file-as="粥左罗" opf:role="aut">粥左罗</dc:creator>
        <dc:date opf:event="publication">2020-09-17</dc:date>
        <dc:identifier opf:scheme="ASIN">B00OUQ6DKQ</dc:identifier>
        <dc:language>zh</dc:language>
        <dc:publisher>与光整理</dc:publisher>
        <dc:title>职场写作与沟通</dc:title>
    </metadata>
    <manifest>
    """
    intermediate = """
        <item href="css/yuguang.css" id="id_Css" media-type="text/css"/>
        <item href="toc.ncx" id="ncx" media-type="application/x-dtbncx+xml"/>
    </manifest>
    <spine toc = "ncx">
    """
    contentAfter = """
    </spine>
        <guide></guide>
    </package>
    """
    manifestContent = ""
    spineContent = ""
    for i in list:
        strNumber = dataList.getNumbering(i['number'])
        manifestContent += """<item href="content/test_%s.html" id="html_%s" media-type="application/xhtml+xml"/>
        """ % (strNumber, strNumber)
        spineContent += """ <itemref idref="html_%s"/>
        """ % (strNumber)
    newPath = path + epubName + fixedNmae[1] + "content.opf"
    content = contentBfter + manifestContent + intermediate + spineContent + contentAfter  # noqa
    with open(newPath, 'wb') as fileName:
        fileName.write(content.encode())
        fileName.close()


# 生成 HTml
def newHtml(contentList, index):
    contentBfter = """
    <?xml version='1.0' encoding='utf-8'?>
    <html xmlns="http://www.w3.org/1999/xhtml" lang="zh-CN" xml:lang="zh-CN">
    <head>
    """ + contentList[0] + """
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link href="../css/yuguang.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
    """
    del (contentList[0])
    contentAfter = """
        </body>
        </html>
    """
    newPath = path + epubName + fixedNmae[2] + "test_" + dataList.getNumbering(
        index) + '.html'
    content = contentBfter + '\r\n'.join(contentList) + contentAfter
    with open(newPath, 'wb') as fileName:
        fileName.write(content.encode())
        fileName.close()


# 图片下载
def newImg(content, imgName):
    newPath = path + epubName + fixedNmae[4] + imgName
    with open(newPath, 'wb') as fileName:
        fileName.write(content)
        fileName.close()
