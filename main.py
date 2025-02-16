
from dotenv import load_dotenv
import os
from loguru import logger

env = os.getenv('env', 'dev')
load_dotenv()
msg = f'hello world! env is {env}'
print('print message')
logger.info(msg)