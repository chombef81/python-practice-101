import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S') 
# logging.debug('this is a debug message')
# logging.info('this ia an infor message')
# logging.warning('this is a warning message')
# logging.error('this is a error message')
# logging.critical('this is a critical message')

import helper

logger = logging.getLogger(__name__)

# create handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.warning('this is a warning')
logger.error('this is an error')