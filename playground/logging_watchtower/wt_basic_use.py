import watchtower
import logging
import boto3

# 设置 root 的日志 level 为 INFO
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.addHandler(watchtower.CloudWatchLogHandler(
    log_group_name="log_group_name",
    log_stream_name="log_stream_name",
    boto3_client=boto3.client("logs", region_name="us-west-2"),
))

print(logger.propagate)
print(logger.handlers)
print(logging.BASIC_FORMAT)

if __name__ == "__main__":
    logger.info("Hi")
    logger.info(dict(foo="bar", details={}))
