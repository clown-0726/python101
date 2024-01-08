import json
import os


class PDFJson2Html:
    def __init__(self, json_path):
        self.json_path = json_path
        self.table_content = []

    def run(self):
        with open(self.json_path, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
        tables = json_file['analyzeResult']['tables']
        paragraphs = json_file['analyzeResult']['paragraphs']
        data = {'tables': tables, 'paragraphs': paragraphs}
        file_name = os.path.basename(self.json_path)
        if not os.path.exists('output/json/'):
            os.makedirs('output/json/')
        with open(f"output/json/{file_name}", "w") as f:
            json.dump(data, f)
        for item in tables:
            for cell in item['cells']:
                if cell['content']:
                    spans = [cell['spans'][0]["offset"], cell['spans'][0]["length"]]
                    self.table_content.append([cell['content'], spans])
        html_text = dict()
        for item in paragraphs:
            page, content = self.paragraph_reader(item)
            if page not in html_text.keys():
                html_text[page] = content
            else:
                html_text[page] += content
        for item in tables:
            page, content = self.table_reader(item)
            if page not in html_text.keys():
                html_text[page] = content
            else:
                html_text[page] += content
        if not os.path.exists('output/html/'):
            os.makedirs('output/html/')
        with open(f"output/html/{file_name.replace('json', 'html')}", "w", encoding='utf-8-sig') as f:
            f.write('''<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable {border-collapse: collapse; width: 100%;}\n
                    td, th {border: 1px solid black;padding: 8px; text-align: left;}\n</style>\n</head>\n''')
            f.write('<body>\n')
            for k, v in html_text.items():
                f.write(v)
            f.write('</body>\n')

    def paragraph_reader(self, item):
        paragraph = ''
        role = item.get('role', None)
        page_num = item.get('boundingRegions')[0]['pageNumber']  # 1
        content = item.get('content')
        spans = [item['spans'][0]["offset"], item['spans'][0]["length"]]
        for content_span in self.table_content:
            if content == content_span[0]:
                if spans[0] == content_span[1][0] and spans[1] == content_span[1][1]:
                    return page_num, ''
        if role is None:
            paragraph += f'\t<p>{content}</p>'
        elif role == 'title':
            paragraph += f'<h1>{content}</h1>'
        elif role == 'sectionHeading':
            paragraph += f'<h2>{content}</h2>'
        return page_num, paragraph + '\n'

    def table_reader(self, item):
        table = '<table>\n'
        page_num = item.get('boundingRegions')[0]['pageNumber']
        rowCount = item.get('rowCount')
        rows = {k: None for k in range(rowCount)}
        for cell in item['cells']:
            meta = [cell['content'], cell.get('columnSpan', None), cell.get('rowSpan', None)]
            if rows[cell['rowIndex']] is None:
                rows[cell['rowIndex']] = [meta]
            else:
                rows[cell['rowIndex']].append(meta)
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
        return page_num, table + '</table>\n'


if __name__ == '__main__':
    for pdf_json_path in os.listdir('input'):
        pdf_json_extract = PDFJson2Html(os.path.join('input', pdf_json_path))
        pdf_json_extract.run()
