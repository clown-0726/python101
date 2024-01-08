from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTFigure, LAParams, LTChar

try:
    page_layouts = extract_pages('xxx.pdf')
    for page_layout in page_layouts:
        print(page_layout.pageid)
        index = 0
        if page_layout.pageid != 5:
            continue

        for element in page_layout:
            if isinstance(element, LTTextContainer):
                sentence = element.get_text()
                print(sentence)
                # 过滤句子太短
                # if len(sentence) < 5:
                #     return False

            if isinstance(element, LTFigure):
                sentence = ''
                for item in element:
                    if isinstance(item, LTChar):
                        # print(item.get_text())
                        # print(item.x0, item.x1, item.y0, item.y1)
                        sentence += item.get_text()
                print(sentence)

except Exception as e:
    print(e)
