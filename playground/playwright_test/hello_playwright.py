import time
from playwright.sync_api import sync_playwright, Page

"""
同步方式运行

pip install playwright
playwright install
"""


def run_in_page(page: Page):
    page.goto("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(100)


def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set headless to False
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    try:
        run_in_page(page)
    except Exception as e:
        print(e)

    context.close()
    browser.close()


with sync_playwright() as p:
    run(p)
