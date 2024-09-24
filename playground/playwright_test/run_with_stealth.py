import time
from playwright.sync_api import sync_playwright, Page
from playwright_stealth import stealth_sync

"""
通过网站 https://brightdata.com/blog/how-tos/avoid-bot-detection-with-playwright-stealth 检测是否会被认为是爬虫
推荐在运行的时候使用 playwright_stealth 进行反爬虫设置
"""


def run_in_page(page: Page):
    page.goto("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(100)


def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set headless to False
    context = browser.new_context()
    page = context.new_page()

    # 使用 stealth 插件
    stealth_sync(page)

    try:
        run_in_page(page)
    except Exception as e:
        print(e)

    context.close()
    browser.close()


with sync_playwright() as p:
    run(p)
