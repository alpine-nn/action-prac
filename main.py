
from dotenv import load_dotenv
import os
import sys
from loguru import logger

env = os.getenv('env', 'dev')
load_dotenv()
msg = f'hello world! env is {env}'
print('print message')
logger.info(msg)
sys.exit(0)