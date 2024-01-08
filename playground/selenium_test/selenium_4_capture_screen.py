import base64
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.baidu.com/")

origin_element = driver.find_element(By.ID, "kw")

# 得到一个元素的截图
# origin_element.screenshot('screen.png')

# 通过得到 base64 保存图片
# x = origin_element.screenshot_as_base64
# image = base64.b64decode(x)
# with open('screen.jpg', "wb") as f:
#     f.write(image)

# 通过二进制的方法进行保存图片到本地
# x = origin_element.screenshot_as_png
# with open('screen.jpg', "wb") as f:
#     f.write(x)

# # 得到可视化区域的截图
# driver.get_screenshot_as_file('screen_full.png')

# # 通过得到 base64 保存图片
# x = driver.get_screenshot_as_base64()
# image = base64.b64decode(x)
# with open('screen_full.jpg', "wb") as f:
#     f.write(image)

# # 截图保存在本地
# driver.save_screenshot('screen_full.png')
#
# # 通过二进制的方法进行保存图片到本地
x = driver.get_screenshot_as_png()
with open('screen_full.jpg', "wb") as f:
    f.write(x)

# ----------

time.sleep(3)
driver.quit()

if __name__ == '__main__':
    pass
