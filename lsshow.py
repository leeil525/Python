import requests
import re
import os

def get_number(number1='2'):#有时候1行2不行 2是高清
    headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
              'Upgrade - Insecure - Requests': '1'
              }
    audio='https://www.lsshow.com/xiuren/xiurenv/728' #这里输入视频当前网址
    abc=requests.get(audio)
    aa = re.search('file=\'.*?\'', abc.text).group(0)
    aa=aa.split('\'')[1]
    number = 1
    while(1):
        a='https://s1.meinazi.com/convert_file/2018/05/'+aa+'/'+number1+'/index'
        url = a + str(number).rjust(4,'0') + '.ts'
        name = str(number)
        try:
            get = requests.get(url,headers=headers,verify=False)
            if(get.status_code) == 404 :
                raise ValueError
        except :
            print('Get False:',url)
            break
        else :
            with open(r'C:\Users\jack\Desktop\movie\down\\' + name + '.ts', 'wb') as file:
                file.write(get.content)
                file.close()
        number=number+1
        print(get.url)

get_number()
# if(number<=2):
#     get_number('1')
os.chdir(r'C:\Users\jack\Desktop\py_file')
os.system('py -3 TStogether.py')

