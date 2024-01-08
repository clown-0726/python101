from orbitkit.pdf_extractor.pdf_block_extractor_v2 import PdfBlockExtractV2
import tracemalloc
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    tracemalloc.start()

    pdf_block_extract_v2 = PdfBlockExtractV2.from_local_file(local_path='xxx.pdf', extend_meta={'xxx': 'xxx'})
    sentence_list = pdf_block_extract_v2.extract()

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10 ** 6}MB, Peak was {peak / 10 ** 6}MB.")

    for sentence in sentence_list:
        print(sentence)

    tracemalloc.stop()
