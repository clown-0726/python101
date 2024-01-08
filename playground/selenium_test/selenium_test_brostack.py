from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BROWSERSTACK_URL = 'https://lilucao1:NBq2Jh4m3qwSbLAq9znm@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
    'os_version': 'Sierra',
    'resolution': '1920x1080',
    'browser': 'Chrome',
    'browser_version': 'latest',
    'os': 'OS X'
}

driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)

driver.get("https://www.sedar.com/search/search_form_pc_en.htm")
driver.get(
    "https://www.sedar.com/FindCompanyDocuments.do?lang=EN&page_no=2&company_search=All+%28or+type+a+name%29&document_selection=0&industry_group=A&FromDate=01&FromMonth=02&FromYear=2020&ToDate=31&ToMonth=02&ToYear=2020&Variable=Issuer"
)

cookies_obj = {}

print(driver.title)
print(driver.page_source)
cookies = driver.get_cookies()
driver.quit()

#
# request_url = 'https://www.sedar.com/FindCompanyDocuments.do?lang=EN&page_no=4&company_search=All+%28or+type+a+name%29&document_selection=0&industry_group=A&FromDate=08&FromMonth=01&FromYear=2020&ToDate=08&ToMonth=01&ToYear=2020&Variable=Issuer'
# content = requests.get(url=request_url, headers=headers)
#
# print(content.text)
