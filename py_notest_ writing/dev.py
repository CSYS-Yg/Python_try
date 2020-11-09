import dataList
import newEpubStructure

getUrl = "https://note.youdao.com/yws/public/notebook/e2574ee5dd46d31b7a500a57961b9b72/subdir/B0BD9A961ACF4DC085333BB455FB6E99"
getId = "B0BD9A961ACF4DC085333BB455FB6E99"
# https://note.youdao.com/yws/public/note/62218d1d8f42aea18e84d345e0e6923d/00C9E44A34884B0CA786F35C11EFEA02?editorType=1&unloginId=7bf14339-5843-ffe1-7965-21e3ea1487ae&editorVersion=new-json-editor

path = "F:\EpubText\/"  # 指定存取目录

epubName = "zhichangxiezuoyugoutong"  # 设置书名，最好为英文

# # 生成指定目录
newEpubStructure.newFolder(path, epubName)
newEpubStructure.newCss()
# # 执行数据抓取
dataList.refining(getUrl)
