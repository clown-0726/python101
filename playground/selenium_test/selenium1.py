from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

if __name__ == '__main__':
    options = ChromeOptions()
    driver = Chrome(ChromeDriverManager().install(), options=options)

    driver.get("https://www.baidu.com/")

    input = driver.find_element(By.ID, 'kw')
    input.send_keys('Hello selenium')


    driver.maximize_window()
    driver.minimize_window()
    driver.fullscreen_window()
    driver.add_cookie()
    driver.delete_cookie()
    driver.delete_all_cookies()


    time.sleep(3)
    driver.quit()
