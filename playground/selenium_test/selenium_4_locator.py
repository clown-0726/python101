from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.baidu.com/")

# 定位到一个基准元素
origin_element = driver.find_element(By.ID, "password")

# 找基准元素上面的 input
above_locator = locate_with(By.TAG_NAME, "input").above(origin_element)
# 找基准元素下面的 input
below_locator = locate_with(By.TAG_NAME, "input").below(origin_element)
# 找基准元素左边的 input
to_left_of_locator = locate_with(By.TAG_NAME, "input").to_left_of(origin_element)
# 找基准元素右边的 input
to_right_of_locator = locate_with(By.TAG_NAME, "input").to_right_of(origin_element)
# 找基准元素最近的 input
near_locator = locate_with(By.TAG_NAME, "input").near(origin_element)

# 联合使用，可以同时使用多个相对定位器来定位一个目标元素
combine_locator = locate_with(By.TAG_NAME, "input") \
    .above(origin_element) \
    .below(origin_element) \
    .to_left_of(origin_element) \
    .to_right_of(origin_element)

time.sleep(3)
driver.quit()

if __name__ == '__main__':
    pass
