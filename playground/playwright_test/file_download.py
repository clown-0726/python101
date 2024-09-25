import asyncio
import time
from playwright.async_api import async_playwright, Error

"""
https://www.idx.co.id/StaticData/NewsAndAnnouncement/ANNOUNCEMENTSTOCK/From_EREP/202403/1483219765_72d8de0178.pdf
这个连接在公司环境下是能下载的，但是挂上 VPN 就没法下载了，有 Cloudflare 的保护！

p.chromium 无法在有头模式下下载 PDF，因为 chromium 默认会展示 PDF
但是通过 p.firefox 可以做到有头模式下的下载操作
"""


async def download_pdf():
    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(headless=False)  # 使用无头模式
        context = await browser.new_context(
            accept_downloads=True,
            bypass_csp=True,
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        )

        page = await context.new_page()
        pdf_url = 'https://www.idx.co.id/StaticData/NewsAndAnnouncement/ANNOUNCEMENTSTOCK/From_EREP/202403/1483219765_72d8de0178.pdf'

        try:
            # 监听下载事件
            async with page.expect_download() as download_info:
                await page.set_content(f'<a href="{pdf_url}">Download</a>')
                await page.click('a')

                content = await page.content()
                print(content)

                # 获取下载对象并保存文件
                download = await download_info.value
                await download.save_as(r'/Users/crown/Projects/python101/playground/playwright_test/your_file1.pdf')

            time.sleep(10)
        except Error as e:
            print(f"An error occurred: {e}")

        finally:
            await browser.close()


# 运行异步任务
asyncio.run(download_pdf())
