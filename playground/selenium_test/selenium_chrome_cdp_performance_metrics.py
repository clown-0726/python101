from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://www.duckduckgo.com')
driver.execute_cdp_cmd('Performance.enable', {})
t = driver.execute_cdp_cmd('Performance.getMetrics', {})
print(t)

time.sleep(10)
driver.quit()

if __name__ == '__main__':
    pass
