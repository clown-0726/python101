from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
options.add_experimental_option('debuggerAddress', '127.0.0.1:9221')
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://my-location.org/")

time.sleep(10)
driver.quit()

if __name__ == '__main__':
    pass
