from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

# 访问 baidu 并打发送 Hello selenium 到输入框
driver.get("https://www.baidu.com/")
input = driver.find_element(By.ID, 'kw')
input.send_keys('Hello selenium')

time.sleep(3)

# 生成一个新的 tab，访问 baidu 并打发送 Hello selenium 到输入框
driver.switch_to.new_window('tab')
driver.get("https://www.baidu.com/")
input = driver.find_element(By.ID, 'kw')
input.send_keys('Hello selenium')

time.sleep(3)

# 生成一个新的 window，访问 baidu 并打发送 Hello selenium 到输入框
driver.switch_to.new_window('window')
driver.get("https://www.baidu.com/")
input = driver.find_element(By.ID, 'kw')
input.send_keys('Hello selenium')

# 得到所有的 windows
win_handles = driver.window_handles
# 遍历这些 windows 并切换到每一个打印其 title
for item in win_handles:
    driver.switch_to.window(item)
    print(item, driver.title)

time.sleep(10)
driver.quit()

if __name__ == '__main__':
    pass
