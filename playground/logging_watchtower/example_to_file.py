import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

# 文件 Handler
file_handler = logging.FileHandler("log.txt")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 标准输出 Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 在 logger 中应用这两个 Handler
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
