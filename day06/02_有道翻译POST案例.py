import requests
import json
import time
import random
import hashlib
# 处理表单数据
# Form表单的数据要放到字典中,然后再进行编码转换

# 加盐方法
def getSalt():
    return str(int(time.time()*1000)+random.randint(0,11))

# 获取sign
def getSign(key,salt):
    #print(key)
    #print(salt)
    sign = ("fanyideskweb" + key + salt + "6x(ZHw]mwzX#u0V7@yfwK")
    hashObj = hashlib.md5()
    hashObj.update(sign.encode("utf-8"))
    return hashObj.hexdigest()

word = input("请输入要翻译的内容:")
saltInfo = getSalt()
data = {"i":word,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":saltInfo,
        "sign":getSign(word,saltInfo),
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false"
    }

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla5.0/"}
res = requests.post(url,data=data,headers=headers)
res.encoding = "utf-8"
result = res.text
print(result)

# 把json格式的字符串转换为 Python字典
# json模块中的loads方法 ：json格式字符串 -> Python字典
#result_dict = json.loads(result)
#r = result_dict["translateResult"][0][0]["tgt"]
#print(r)

































