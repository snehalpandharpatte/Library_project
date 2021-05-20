from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import logging
import time

logger = logging.getLogger("second")
# logger.info("In welcome page of second app")

def welcome_page(request):
    # logger.info("In welcome page of second app")
    # for i in range(1,10):
    #     logger.info(f"--------------{i}---------------")
    #     logger.debug("This debug level")
    #     logger.info("This info level")
    #     logger.warning("This warning level")
    #     logger.error("This error level")
    #     logger.critical("This critical level")
    #     time.sleep(1)
    
    logger.debug("This debug level")
    logger.info("This info level")
    logger.warning("This warning level")
    logger.error("This error level")
    logger.critical("This critical level")
    time.sleep(1)

        # try:
        #     l = [100,250,300]
        #     l[0]   #index error
        #     # l[0]  #no error
        #     logger.debug(f"{l[0]}") 
        #     # logger.debug(f"{l[5]}")

        # except IndexError as msg:
        #     logger.exception(msg)   #error/exception
        #     return HttpResponse("IndexError")
    return HttpResponse("Hello----this is welcome view")
    