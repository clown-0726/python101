from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.baidu.com/")

# 定义查找的 locator
locator = (By.ID, 'kw')
# 通过 EC 和 locator 定义要显示等待的条件，并声明等待的行为
WebDriverWait(driver=driver,
              timeout=20,
              poll_frequency=0.5,
              ignored_exceptions=None).until(EC.presence_of_element_located(locator))

'''
EC.title_is
EC.element_to_be_clickable
EC.alert_is_present
EC.element_located_to_be_selected
......
'''

input = driver.find_element(By.ID, 'kw')
input.send_keys('Hello selenium')

time.sleep(3)
driver.quit()

if __name__ == '__main__':
    pass
