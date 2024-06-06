import logging

# 对 root logger 的设置
logging.basicConfig(level=logging.INFO)  # 设置 root 的日志 level 为 INFO
print(logging.BASIC_FORMAT)  # %(levelname)s:%(name)s:%(message)s
print(logging.root.handlers)  # [<StreamHandler <stderr> (NOTSET)>]

# 设置自定义的 logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
# logger.propagate = False # 可以设置为不传播
# print(logger.propagate)  # 其默认的 propagate 为 True，会将 log 代理到其父级
# print(logger.parent)     # 查看其父级的 handler


if __name__ == "__main__":
    logger.info("Hi")
    logger.info(dict(foo="bar", details={"skill": "java"}))
