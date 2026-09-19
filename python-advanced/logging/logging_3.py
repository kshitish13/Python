import logging

logger=logging.getLogger('mylogger')

logger.setLevel(logging.DEBUG)
file_handler=logging.FileHandler("my_app.log")
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#logging messages
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')