from typing import Optional, List

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTFigure, LTChar
from orbitkit import id_srv
from Crypto.Cipher import AES

"""
>>> 注意事项 <<<
pdfminer.six page 索引是从 1 开始的
pdfplumber page 索引是从 0 开始的
本程序的索引是从 1 开始的
"""


class PdfBlockExtract:
    def __init__(self, local_path: str, extend_meta: dict, pages: Optional[List[int]] = None):
        self.local_path = local_path
        self.pages = pages
        self.extend_meta = extend_meta
        self.sentence_list = []

    def sentence_filter(self, sentence: str):
        sentence = sentence.strip()
        is_valid_sentence = True
        if sentence == '':
            is_valid_sentence = False
        if len(sentence) < 3:
            is_valid_sentence = False
        return {
            'sentence': sentence,
            'is_valid_sentence': is_valid_sentence,
        }

    def loop_pages(self, page_layout):
        index = 1
        for element in page_layout:
            # 如果页面的元素是 LTTextContainer 则直接拿数据
            if isinstance(element, LTTextContainer):
                sentence = element.get_text()
                # Filter sentence
                sentence_obj = self.sentence_filter(sentence)
                if sentence_obj['is_valid_sentence'] is False:
                    continue
                sentence = sentence_obj['sentence']

                _txt_data = {
                    "id": f"l_{id_srv.get_random_short_id()}",
                    "page": str(page_layout.pageid),
                    "seq_no": str(index),
                    "sentence": sentence,
                    "type": "sentence",
                    "text_location": {
                        "location": [[element.x0, element.y1, element.x1, element.y0]]
                    }
                }
                _txt_data.update(self.extend_meta)  # 合并额外信息
                self.sentence_list.append(_txt_data)
                index += 1

            # 如果页面的元素是 LTFigure 则拼接字符拿数据
            if isinstance(element, LTFigure):
                sentence_item = ''
                x0_list = []
                y1_list = []
                x1_list = []
                y0_list = []
                location = []
                for item in element:
                    if isinstance(item, LTChar):
                        sentence_item += item.get_text()
                        x0_list.append(item.x0)
                        y1_list.append(item.y1)
                        x1_list.append(item.x1)
                        y0_list.append(item.y0)

                # PDF 可能有空页情况, 或者某一页没提取出坐标 min max 报错
                if len(x0_list) > 0 and len(y1_list) > 0 and len(x1_list) > 0 and len(y0_list) > 0:
                    location.append(min(x0_list))
                    location.append(max(y1_list))
                    location.append(max(x1_list))
                    location.append(min(y0_list))

                    # Filter sentence
                    sentence_obj = self.sentence_filter(sentence_item)
                    if sentence_obj['is_valid_sentence'] is False:
                        continue
                    sentence = sentence_obj['sentence']

                    _txt_data = {
                        "id": f"l_{id_srv.get_random_short_id()}",
                        "page": str(page_layout.pageid),
                        "seq_no": str(index),
                        "sentence": sentence,
                        "type": "sentence",
                        "text_location": {
                            "location": [location]}
                    }
                    _txt_data.update(self.extend_meta)  # 合并额外信息
                    self.sentence_list.append(_txt_data)
                    index += 1

            # 如果两个 if 都匹配不上则说明此 element 没有数据
            pass

    def extract(self):
        """入口方法
        可以根据 specific_page 选择是提取单独一页的数据还是全部解析
        """
        page_layouts = extract_pages(self.local_path)
        # 解析单独一页数据
        if self.pages:
            for page_layout in page_layouts:
                if page_layout.pageid in self.pages:
                    self.loop_pages(page_layout)
        else:
            # 解析所有页面
            for page_layout in page_layouts:
                self.loop_pages(page_layout)

        return self.sentence_list


if __name__ == '__main__':
    pdf_block_extract = PdfBlockExtract('xxx.pdf', {'xxx': 'xxx'})
    sentence_list = pdf_block_extract.extract()
    for item in sentence_list:
        print(item)

    print(len(sentence_list))
