import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(message)s')

if __name__ == '__main__':
    logging.debug('this is debug message')
    logging.info('this is info message')
    logging.warning('this is warning message')

'''''
结果：
2024-06-06 17:10:43,873 - root - this is debug message
2024-06-06 17:10:43,873 - root - this is info message
2024-06-06 17:10:43,873 - root - this is warning message
'''
