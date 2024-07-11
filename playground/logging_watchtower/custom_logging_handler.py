import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)

""" 自定义 logging handler """


class CustomLogHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        print("🤑", log_entry)

    def close(self):
        print("🤑🤑🤑🤑🤑🤑")
        super().close()


if __name__ == '__main__':
    logging.root.addHandler(CustomLogHandler())
    logger.info("xxx")
