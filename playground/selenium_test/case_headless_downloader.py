import datetime
import os
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from os.path import abspath, dirname
import tempfile

BASE_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, BASE_DIR)

DOWNLOAD_DIR = dirname(abspath(__file__))
print(DOWNLOAD_DIR)


def is_download_success(tmp_dir, extension):
    '''
    lambda
        - 下载超时时间 10 分钟
        - 空文件检测超时 2 分钟
    '''
    start_timestamp = datetime.datetime.now().timestamp()
    TEN_MINUTES = 60 * 10
    TWO_MINUTES = 60 * 2

    in_while = True
    file_path = ''
    while in_while:
        for root, dirs, files in os.walk(tmp_dir):
            if root != tmp_dir:
                break

            print(files)

            # 如果多于一个文件说明下载出现问题
            if len(files) > 1:
                raise Exception('Other error...')

            # 如果没有文件，并且时间超过 2 分钟，表示下载异常
            if len(files) == 0:
                delta_sec = int(datetime.datetime.now().timestamp() - start_timestamp)
                if delta_sec > TWO_MINUTES:
                    raise Exception('Download timeout...no file')

            # 如果只有一个文件，并且满足下载的后缀名，则说明下载成功
            if len(files) == 1 and str(files[0]).lower().endswith('.' + extension):
                in_while = False
                file_path = os.path.join(root, files[0])

        time.sleep(1)

        # 如果整体的下载时间超过 10 分钟，表示下载异常
        delta_sec = int(datetime.datetime.now().timestamp() - start_timestamp)
        if delta_sec > TEN_MINUTES:
            raise Exception('Download timeout...total')
    return file_path


'''
Start chrome driver
'''
options = webdriver.ChromeOptions()
# 防指纹操作
# options.add_argument("start-maximized")
options.add_argument("--window-size=1325x744")
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

with tempfile.TemporaryDirectory() as tmp_dir:
    options.add_experimental_option('prefs', {
        # "download.default_directory": tmp_dir,  # Change default directory for downloads
        "download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,  # It will not show PDF directly in chrome
    })

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Headless 模式下要这种设置才能指定下载路径
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {'behavior': 'allow', 'downloadPath': tmp_dir}
    }
    driver.execute("send_command", params)

    # 防指纹操作
    with open('./stealth.min.js') as f:
        inject_js = f.read()
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": inject_js})

    print('xxxxx')
    # driver.get(url='https://www.greencoat-ukwind.com/~/media/Files/G/GreenCoat-UKWind/documents/modern-slavery-statement-2022.pdf')
    driver.get(url='https://pdflux.com/downloads/PDFlux-latest.dmg')  # .crdownload
    # driver.get(url='https://www.comerica.com/content/dam/comerica/en/documents/resources/about/sustainability/2020-comerica-cr-report-final.pdf')

    is_download_success(tmp_dir, '.dmg')

    if driver:
        driver.quit()

if __name__ == '__main__':
    pass

'''
{
  "id": "", 要更新的 db 字段
  "url": "", 下载地址
  "file_type": "pdf",
  "store_path_folder": "" s3 存储文件夹
}

'''
