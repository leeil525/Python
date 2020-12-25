# import requests
# r=requests.get("http://baidu.com") #获取一个网站的代码
# params={'abc':'def','yyy':'kkk'}
# 也可以传入参数 r=requests.get("**",params=params)  http://baidu.com/?abc=def&yyy=kkk
# r.content 返回二进制 音乐 视频
# r.json() 返回JSON格式
# r.status_code 返回成功为200
# r.text 返回解析的结果
>>> r.encoding='utf-8'
>>> print(r.text)  中文
# r.headers 返回请求头部 可以在请求的时候修改头部 r=requests.get('',headers=headers)
# r.cookies Cookies传递 r=requests.get('',cookies=dict(a='b'))
# r=requests.post("http://www.baidu.com",data={'key':'value'}) POST请求 加密发送的信息 密码
# r=requests.post("*",files=files) files={'file':open('aa.xls','rb')}
# r=requests.get("http://baidu.com",timeout=0.1) #设置时间
#s=requests.Session()   自动保存cookies，可以设置请求参数，下次请求自动带上请求参数
#s.get('http://www.***.com')
#r=s.get('http://www.***.com')
#r=requests.get("http://baidu.com",verify=False) 忽略证书验证SSL
#r = requests.get(url, stream=True) 只有响应头部下载下来 然后验证头部再
#决定 r.headers['content-length'] < 999  content=r.content 需读取所有数据
#再关闭 也可以使用Response.close










