from us_visa.logger.logging import logging as custom_log
from us_visa.exception.Custom_exception import USvisaException
import sys

#custom_log.info("Welcome to our custom log")


try:
    a = 2/0

except Exception as e:
    raise USvisaException(e,sys)