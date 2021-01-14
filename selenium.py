from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #输入的键盘位键操作
from selenium.webdriver.support.ui import Select  #选项卡操作
from selenium.webdriver import ActionChains  #拖拽元素
from selenium.webdriver.chrome.options import Options #设置Chrome手机模式
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities #设置PhantomJS手机模式


#browser = webdriver.PhantomJS(executable_path='D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe') PhantomJS 用法
#browser=webdriver.Chrome()


'''PhantomJs手机模式并截图'''
# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
# "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
# )
# driver = webdriver.PhantomJS(desired_capabilities=dcap)
# driver.get("https://bilibili.com")
# driver.get_screenshot_as_file('02.png')
# driver.quit()



'''Chrome手机模式'''
# mobile_emulation = {"deviceName":"Apple iPhone 6"}
# chrome_options = Options()
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# browser = webdriver.Chrome(chrome_options=chrome_options)  # 手机模式浏览
# browser.get("http://www.bilibili.com")            #打开bilibili

'''查找元素'''

#element = browser.find_element_by_id("q")                  #根据ID查找 
#element = browser.find_element_by_css_selector("input")    #根据css选择器查找
#element = browser.find_element_by_name("passwd")           #根据name属性查找 name='passwd'
#element = browser.find_elements_by_tag_name("input")       #根据标签查找<input></input>
#element = browser.find_element_by_xpath('//*[@id="banner_link"]/div/div/form/input')  #根据XPATH语法查找（搜索输入框）
#上面是单个 在element后加s就OK  


'''向表单填写,按键，点击'''
#element.send_keys("test") #写入test
#element.clear() #清除之前的文本
#element.send_keys("test2") #写入test
#element.send_keys(Keys.RETURN)  #模拟按enter
#element.click()  #鼠标点击

'''选项卡操作'''
#select = Select(driver.find_element_by_name('name')) 
#select.select_by_index(index)         #根据索引来选择
#select.select_by_visible_text("text") #根据值来选择
#select.select_by_value(value)         #根据文字来选择
#select.deselect_all()                 #取消全部的选择

'''拖拽元素'''
#element2 = browser.find_element_by_xpath('//*[@id="banner_link"]/div/div/form/input')
#element1 = browser.find_element_by_xpath('//*[@id="banner_link"]/div/div/a')
#action_chains = ActionChains(browser)
#action_chains.drag_and_drop(element2, element1).perform()  #2拖到1
#ActionChains(browser).drag_and_drop_by_offset(element2,10,10).perform() #把element2拖动（10，10）的距离，即向右下方拖动


#browser.close() #关闭浏览器


















