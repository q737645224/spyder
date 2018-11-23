import requests
import json

# 处理表单数据
# Form表单的数据要放到字典中,然后再进行编码转换
word = input("请输入要翻译的内容:")
data = {"i":word,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"1536648321283",
        "sign":"1e7948e25551448dbfb7184f23dc126c",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false"
    }

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla5.0/"}
res = requests.post(url,data=data,headers=headers)
res.encoding = "utf-8"
result = res.text

# 把json格式的字符串转换为 Python字典
# json模块中的loads方法 ：json格式字符串 -> Python字典
result_dict = json.loads(result)
r = result_dict["translateResult"][0][0]["tgt"]
print(r)

































