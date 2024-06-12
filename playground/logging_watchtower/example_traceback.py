import logging

logger = logging.getLogger(__name__)

try:
    open('/path/to/does/not/exist', 'rb')
except Exception as e:
    logger.error('Failed to open file', exc_info=True)

'''
Failed to open file
Traceback (most recent call last):
  File "/Users/crown/Projects/python101/playground/logging_watchtower/example_traceback.py", line 6, in <module>
    open('/path/to/does/not/exist', 'rb')
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/does/not/exist'
'''
