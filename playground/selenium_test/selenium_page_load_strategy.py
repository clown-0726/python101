from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
options.page_load_strategy = 'normal'
# options.page_load_strategy = 'eager'
# options.page_load_strategy = 'none'

driver = Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://www.baidu.com/")

time.sleep(10)
driver.quit()

'''
normal	complete	默认情况下使用, 等待所有资源下载完成
eager	interactive	DOM访问已准备就绪, 但其他资源 (如图像) 可能仍在加载中
none	Any	完全不阻塞WebDriver
'''

if __name__ == '__main__':
    pass
