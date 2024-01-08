from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

if __name__ == '__main__':
    options = ChromeOptions()
    driver = Chrome(ChromeDriverManager().install(), options=options)

    # 全局设置，在需要等待元素出现的地方最多等待 30 秒
    driver.implicitly_wait(30)

    driver.get("https://www.baidu.com/")

    input = driver.find_element(By.ID, 'kw')
    input.send_keys('Hello selenium')

    time.sleep(3)
    driver.quit()
