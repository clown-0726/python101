from urllib.parse import urlparse


def parse_other_schema():
    url = "postgresql://ddd:ccc@pgm-2zeufgdfe28y14810zm.pg.rds.aliyunc.com:1921/stockcn_test"
    parsed = urlparse(url)

    print("scheme: ", parsed.scheme)
    print("username: ", parsed.username)
    print("password: ", parsed.password)
    print("hostname: ", parsed.hostname)
    print("port: ", parsed.port)
    print("path: ", parsed.path)
    print("netloc: ", parsed.netloc)


def parse_http_schema():
    url_list = [
        "https://zuleikagold.com.au",
        "https://www.masholdings.co.zw/",
        "http://khayahcement.co.zw/",
        "https://www.innscorafrica.com",
        "https://www.tongaat.com/hippo-valley-estates/company-profile/",
        "http://www.gbholdings.co.zw/",
        # Below is invalid
        "www.meiklesltd.com/",
        "hwangecolliery.co.zw/",
    ]

    for url in url_list:
        parsed = urlparse(url)

        print(f"👻👻👻{url} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("SCHEME: ", parsed.scheme)
        print("HOSTNAME: ", parsed.hostname)
        print("PORT: ", parsed.port)
        print("PATH: ", parsed.path)


if __name__ == "__main__":
    parse_other_schema()
    parse_http_schema()
