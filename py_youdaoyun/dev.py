import dataList
import newEpubStructure

getUrl = "https://note.youdao.com/yws/public/notebook/62218d1d8f42aea18e84d345e0e6923d/subdir/9D3030DCC7734AC3BBA0A01DAECF50B0"
getId = "62218d1d8f42aea18e84d345e0e6923d"
# https://note.youdao.com/yws/public/note/62218d1d8f42aea18e84d345e0e6923d/00C9E44A34884B0CA786F35C11EFEA02?editorType=1&unloginId=7bf14339-5843-ffe1-7965-21e3ea1487ae&editorVersion=new-json-editor

newEpubStructure.newFolder()
dataList.refining(getUrl)
