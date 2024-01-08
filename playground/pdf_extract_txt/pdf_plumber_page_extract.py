import pdfplumber
import tracemalloc

tracemalloc.start()

with pdfplumber.open('xxx.pdf') as pdf:
    total_pages = pdf.pages

for pdf_page in total_pages:
    with pdfplumber.open('xxx.pdf') as pdf:
        print(f"****************************************** {str(pdf_page.page_number)} ******************************************")
        pdf.pages[pdf_page.page_number - 1].extract_text()

        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage is {current / 10 ** 6}MB, Peak was {peak / 10 ** 6}MB.")

        # for page in pages:
        #     print(f"****************************************** {str(page.page_number)} ******************************************")
        #     # page.extract_text()
        #     page.extract_tables()
        #     page.flush_cache()
        #
        #     current, peak = tracemalloc.get_traced_memory()
        #     print(f"Current memory usage is {current / 10 ** 6}MB, Peak was {peak / 10 ** 6}MB.")

tracemalloc.stop()

if __name__ == '__main__':
    pass
