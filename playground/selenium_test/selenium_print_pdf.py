from base64 import b64decode
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.print_page_options import PrintOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--headless")
options.accept_insecure_certs = True
driver = Chrome(ChromeDriverManager().install(), options=options)

print_options = PrintOptions()
print_options.page_ranges = ['1-2']

driver.get("https://www.baidu.com/")
print(driver.title)
base64_code = driver.print_page(print_options)

with open('page.pdf', 'wb') as f:
    f.write(b64decode(base64_code.encode("ascii")))

time.sleep(30)
driver.quit()

if __name__ == '__main__':
    pass
