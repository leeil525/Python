
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mobile_emulation = {"deviceName":"Apple iPhone 6"}
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.baidu.com")