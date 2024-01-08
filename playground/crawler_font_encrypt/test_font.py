import requests
from fontTools.ttLib import TTFont
from lxml import etree

fonturl = 'http://shanzhi.spbeen.com/static/fonts/szec.ttf'
fontresponse = requests.get(fonturl)

# with open('font.ttf', 'wb') as file:
#     file.write(fontresponse.content)

font = TTFont('font.ttf')
result_dict = {}
for k, v in font['cmap'].getBestCmap().items():
    k = hex(k).replace('0x', '&#x') + ';'
    v = int(v[8:10]) - 1
    result_dict[k] = str(v)

print(result_dict)

url = 'http://shanzhi.spbeen.com/search/?word='
response = requests.get(url)
html = response.text
for k, v in result_dict.items():
    html = html.replace(k, v)
# print(html)

htmlobj = etree.HTML(html)
divcard = htmlobj.xpath('.//div[@class="content"]/div')
for dc in divcard:
    td = {}
    td['标题'] = dc.xpath('./div/h5/a/text()')
    td['薪资'] = dc.xpath('./div/h5/a/text()')
    print(td)

if __name__ == '__main__':
    pass
