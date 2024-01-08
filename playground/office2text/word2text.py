import docx

'''
pip install python-docx

参考连接：https://qa.1r1g.com/sf/ask/1765967451/
'''


def get_text(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


all_text = get_text('./asset/django_reset_frame_work.docx')
print(all_text)

if __name__ == '__main__':
    pass
