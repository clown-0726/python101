import logging

format_str = '%(levelname)s %(filename)s %(document_id)s %(message)s'
logging.basicConfig(level=logging.INFO, format=format_str)

logger = logging.getLogger(__name__)

extra = {'document_id': 'doc id'}
logger = logging.LoggerAdapter(logger, extra)

logger.info({'name': 'Xiao Ming'})
