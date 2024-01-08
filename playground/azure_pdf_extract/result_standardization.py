"""
    Azure提取文本结果标准化
"""
from orbitkit import id_srv
import json
import os


# pip install azure-keyvault-secrets
# pip install azure-core
# pip install azure-ai-formrecognizer


class ResultStandardization:
    """
    Azure提取文本结果标准化
    :param res: AnalyzeResult Azure提取结果
    """

    def __init__(self, res):
        self.result = res
        self.pdf_height = dict()
        for page in self.result.pages:
            self.pdf_height[page.page_number] = page.height
        self.table_content = []

    def paragraph_reader(self, item):
        """
        解析一条段落记录
        """
        page_num = item.bounding_regions[0].page_number
        polygon = item.bounding_regions[0].polygon
        # Azure polygon 坐标转换
        location = [float(i) * 72 for i in [polygon[0][0], self.pdf_height[page_num] - polygon[0][1], polygon[2][0], self.pdf_height[page_num] - polygon[2][1]]]
        content = item.content
        # 通过 content, offset 和 length 判断是否为表格中的内容, 若是则去重
        spans = [item.spans[0].offset, item.spans[0].length]
        for content_span in self.table_content:
            if content == content_span[0]:
                if spans[0] == content_span[1][0] and spans[1] == content_span[1][1]:
                    return page_num, None
        meta = {
            "id": "l_" + id_srv.get_random_short_id(),
            "page": page_num,
            "seq_no": 0,
            "sentence": content,
            "type": "sentence",
            "text_location": {"location": [location]},
        }
        return page_num, meta

    def table_reader(self, item):
        """
        解析一条表格记录
        """
        page_num = item.bounding_regions[0].page_number
        polygon = item.bounding_regions[0].polygon
        # Azure polygon 坐标转换
        location = [float(i) * 72 for i in [polygon[0][0], self.pdf_height[page_num] - polygon[0][1], polygon[2][0], self.pdf_height[page_num] - polygon[2][1]]]

        # 表格分行
        rows = {k: None for k in range(item.row_count)}
        for cell in item.cells:
            cell_info = [cell.content, cell.column_span, cell.row_span]
            if rows[cell.row_index] is None:
                rows[cell.row_index] = [cell_info]
            else:
                rows[cell.row_index].append(cell_info)

        # 表格转html
        table = '<table>\n'
        for k, tds in rows.items():
            tr = '\t<tr>\n'
            if tds:
                for meta in tds:
                    tr += '\t\t<td'
                    if meta[1]:
                        tr += f' colspan="{str(meta[1])}"'
                    if meta[2]:
                        tr += f' rowspan="{str(meta[2])}"'
                    tr += f'>{meta[0]}</td>\n'
            tr += '\t</tr>\n'
            table += tr
        table += '</table>\n'

        meta = {
            "id": "l_" + id_srv.get_random_short_id(),
            "page": page_num,
            "seq_no": 0,
            "sentence": table,
            "type": "table",
            "text_location": {"location": [location]},
        }
        return page_num, meta

    def standardize2json(self):
        """
        将Azure提取结果转为json列表
        """
        tables = self.result.tables
        paragraphs = self.result.paragraphs

        # 记录表格 offset 和 length 用于段落去重
        for table in tables:
            for cell in table.cells:
                if cell.content:
                    spans = [cell.spans[0].offset, cell.spans[0].length]
                    self.table_content.append([cell.content, spans])

        page_json_set = dict()
        # 段落内容格式化
        for item in paragraphs:
            page, meta = self.paragraph_reader(item)
            if meta:
                if page not in page_json_set.keys():
                    page_json_set[page] = [meta]
                else:
                    page_json_set[page].append(meta)

        # 表格内容格式化
        for item in tables:
            page, meta = self.table_reader(item)
            if page not in page_json_set.keys():
                page_json_set[page] = [meta]
            else:
                for i in range(len(page_json_set[page])):
                    # 根据 text_location 坐标将表格插入到段落中
                    if meta['text_location']['location'][0][1] > page_json_set[page][i]['text_location']['location'][0][1]:
                        page_json_set[page].insert(i, meta)
                        break
                    if i == len(page_json_set[page]) - 1:
                        page_json_set[page].append(meta)

        # 句子顺序编号
        db_record_list = []
        for page, json_list in page_json_set.items():
            for i, j in enumerate(json_list):
                j['seq_no'] = i + 1
                db_record_list.append(j)

        return db_record_list

    def result_txt_writer(self, output_path):
        record_list = self.standardize2json()
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # block.txt
        with open(os.path.join(output_path, 'blocks.txt'), 'w+', encoding='utf-8') as f:
            for i in record_list:
                f.write(json.dumps(i, ensure_ascii=False) + '\n')

        # pages.txt
        page_list = {}
        for i in record_list:
            if i['page'] not in page_list.keys():
                page_list[i['page']] = i['sentence']
            else:
                page_list[i['page']] += '\n' + i['sentence']
        with open(os.path.join(output_path, 'pages.txt'), 'w+', encoding='utf-8') as f:
            for k, v in page_list.items():
                meta = {
                    "id": "p_" + id_srv.get_random_short_id(),
                    "page": k,
                    "sentence": v
                }
                f.write(json.dumps(meta, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    import pickle

    with open('result.pkl', 'rb') as f:
        result = pickle.load(f)
    '''
    ResultStandardization 类使用方法：
    1、传入 Azure 提取结果 以及 PDF 每页的高度
    2、调用 result_txt_writer 方法，将结果写入到 output 文件夹下的 blocks.txt 和 pages.txt 中
    '''
    # 读取pdf文件，获取pdf每一页的高度
    rs = ResultStandardization(result)
    rs.result_txt_writer(output_path="fake_path")

    # {
    #     'id': 'l_12345678',
    #     'page': 181,
    #     'seq_no': 32,
    #     'sentence': 'Dividend return   \nPaid dividend per share',
    #     'type': 'sentence',
    #     'text_location': {'location': [[555.5906, 344.977, 643.9226, 324.356]]},
    #     'xxx': 'xxx'
    # }
