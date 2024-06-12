import logging

# root logger
logging.basicConfig(level=logging.INFO)

# parent logger
logger_parent = logging.getLogger("parent")
handler = logging.StreamHandler()
handler.setLevel(logging.CRITICAL)  # Set the handler's level to CRITICAL
logger_parent.addHandler(handler)
logger_parent.setLevel(level=logging.CRITICAL)

# child logger
logger_child = logging.getLogger("parent.child")
logger_child.addHandler(logging.StreamHandler())
logger_child.setLevel(level=logging.INFO)

if __name__ == "__main__":
    logger_child.info("Hi")
