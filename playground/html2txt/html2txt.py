import re
from selectolax.parser import HTMLParser


def remove_all_tags_v1(tag_str, substitution=" "):
    """
    :param tag_str:
    :param substitution:
    :return:
    """
    return str(re.sub(r'<.*?>', substitution, tag_str))


if __name__ == '__main__':
    with open("segment.html", "r+", encoding="utf-8") as f:
        target_html = f.read()
        text1 = HTMLParser(target_html).text()
        print(text1)

        text2 = remove_all_tags_v1(target_html)
        print(text2)
