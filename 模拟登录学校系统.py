import requests
from PIL import Image
r=requests.Session()
url=r.get("http://10.20.208.11/")
url=url.url  #实际访问网址
nu=url.find('defau')
jpg_url=url[0:nu]+'CheckCode.aspx'#验证码图片地址
pct=requests.get(jpg_url)
with open('aa.jpg','wb') as file:
	file.write(pct.content)
im=Image.open('aa.jpg')
im.show()
test=input("输入验证码")
data={
'__VIEWSTATE':'dDwxNTMxMDk5Mzc0Ozs+wU36jz/uYAlzKwJzaSDs3+aDrpg=',
'txtUserName':'*',#用户名
'Textbox1':'',
'TextBox2':'*',#密码
'txtSecretCode':test,
'RadioButtonList1':'(unable to decode value)',
'Button1':'',
'lbLanguage':'',
'hidPdrs':'',
'hidsc':''
	}
s1=r.post(url,data)
print(s1.text[:500])






