import requests
from bs4 import BeautifulSoup

r=requests.get("http://bilibili.com")
soup=BeautifulSoup(r.text,'lxml') 熬制一锅汤
print(soup.prettify()) 按格式化输出

***Tag***
soup.title 获取标签这个Tag（有多个就返回第一个）
type(soup.title) <class 'bs4.element.Tag'>
soup.title.name 标签名字
soup.title.attrs 标签属性 返回字典{'class': ['title'], 'name': 'dromouse'} 访问特定的属性soup.title['class']


**NavigableString**可遍历字符串
soup.title.string 获取标签内的内容，会显示注释内容但
不会显示注释符号 type(soup.p.string)=<class 'bs4.element.NavigableString'>
如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。
如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容
里面有多个标签则返回None

***Comment***
如果标签的内容是注释那么type(soup.p.string)=<class 'bs4.element.Comment'>
所以最好判断一下if type(soup.a.string)==bs4.element.Comment:
                       print(soup.a.string)
***


soup.head.contents  以列表形式返回标题的所有儿子
soup.head.childern  儿子 返回list生成器  用遍历  for i in soup.title.childern:print(i)
soup.title.descendants 返回子孙  list生成器 for i in soup.title.descendants:print(i)
soup.strings 返回所有标签内容  生成器
soup.stripped_strings   返回所有标签内容附带去空格 生成器

soup.title.parent 返回节点的父亲
soup.title.parents 返回爸爸和爸爸的爸爸。。。直到<html> 生成器
soup.title.next_sibling 返回下一个兄弟节点 .next_siblings返回生成器
soup.title.previous_sibling  返回上一个兄弟的节点  .previous_siblings返回生成器
soup.title.next_element   返回下一个节点，不是针对于兄弟节点，而是在所有节点，不分层次  soup.title.next_elements 同理 
soup.title.previous_element  返回前一个节点，不是针对于兄弟节点，而是在所有节点，不分层次  soup.title.previous_elements  同理 

tag.has_attr('class') 包含了class元素则返回True

find_all( name , attrs , recursive , text , **kwargs )
soup.find_all('a') 返回所有<a></a>标签的bs数组
soup.find_all(re.compile("^b")) 返回含b的所有标签如<b></b> <bcd></bcd>  返回bs数组
soup.find_all(["a","b"])  返回所有a、b标签

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id)  返回所有含class 不含 id 的标签


soup.find_all(id='link2')   查找id=link2的所有标签
soup.find_all(href=re.compile("elsie"))  查找href满足正则的所有标签
soup.find_all(href=re.compile("elsie"), id='link1')  满足以上两个条件
soup.find_all("a", class_="sister")  class要加下划线

data_soup.find_all(attrs={"data-foo": "value"})  搜索特殊属性的标签


soup.find_all(text="aaa")
soup.find_all(text=["aaa", "bbb", "ccc"])
soup.find_all(text=re.compile("abc"))  这三个是查找文档中字符串的内容

soup.find_all("a", limit=2) 查找a标签 查找到两个时停止并返回


CSS选择器

soup.select('title')     返回所有title标签的数组 list
soup.select('.sister')   返回所有class="sister"标签的数组 list
soup.select('#aa')       返回所有id="aa"标签的数组 list
soup.select('p #aa')     p标签 且 id=aa
soup.select("head > title")  head的子标签title
soup.select('a[class="aa"]')    a标签 and class='aa'
soup.select('a[href="http://www"]')  同上
soup.select('p a[href="http://www"]')  组合 同上





















