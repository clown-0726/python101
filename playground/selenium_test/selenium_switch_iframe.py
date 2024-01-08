from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_height_width_css")

iframes = driver.find_elements(By.TAG_NAME, 'iframe')
print(len(iframes))

# 通过名字切换到下一级的 iframe（名字为 iframeResult）
driver.switch_to.frame('iframeResult')
h2_text = driver.find_element(By.XPATH, '//body/h2')
print(h2_text.text)

# 通过 index 切换到下一级的 iframe（没有名字）
driver.switch_to.frame(0)
h1_text = driver.find_element(By.XPATH, '//body/h1')
print(h1_text.text)

# 切换到上一级的 iframe
driver.switch_to.parent_frame()

time.sleep(3)
driver.quit()

if __name__ == '__main__':
    pass
