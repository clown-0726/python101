from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

# options = ChromeOptions()
# options.add_argument("start-maximized")
# options.accept_insecure_certs = True
# driver = Chrome(ChromeDriverManager().install(), options=options)
#
# driver.get("https://www.baidu.com/")
#
# print(driver.title)
#
# time.sleep(30)
# driver.quit()

options = FirefoxOptions()
options.add_argument("start-maximized")
options.accept_insecure_certs = True
driver = Firefox(GeckoDriverManager().install(), options=options)

driver.get("https://www.baidu.com/")

print(driver.title)

time.sleep(30)
driver.quit()

if __name__ == '__main__':
    pass
