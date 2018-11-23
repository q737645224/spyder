from urllib import request

url = "http://www.renren.com/967469305/profile"
headers = {"Host":"www.renren.com",
           "Connection":"keep-alive",
           "Upgrade-Insecure-Requests":"1",
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Referer":"http://www.renren.com/SysHome.do",
           #Accept-Encoding: gzip, deflate
           "Accept-Language":"zh-CN,zh;q=0.9",
           "Cookie":"anonymid=jlxb586t8i3v0g; depovince=BJ; _r01_=1; JSESSIONID=abcqRp76SQcK0dfdzQhxw; ick_login=4165cad5-4fdc-466c-a7d0-98e014715ff0; first_login_flag=1; ln_uact=13603263409; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; jebe_key=094486d9-6cd0-442c-a7d4-c9115c822ab7%7C2012cb2155debcd0710a4bf5a73220e8%7C1536653132046%7C1%7C1536653131904; wp_fold=0; wp=0; jebecookies=8314ca50-d39d-4df1-b9fa-ea391456cc38|||||; _de=4DBCFCC17D9E50C8C92BCDC45CC5C3B7; p=356eafd62d5adaeb90370c13491ac9055; t=b963e2106aa3249e5289deba7f486e915; societyguester=b963e2106aa3249e5289deba7f486e915; id=967469305; xnsid=3850523b"
    }
req = request.Request(url,headers=headers)
res = request.urlopen(req)
html = res.read().decode("utf-8")
print(html)










