from django.shortcuts import HttpResponse
import logging  # here import login modual : to manage a logger :
# Create your views here.


def home(request):
    logger = logging.getLogger(__name__)
    logger = logging.getLogger("myapp")  # HEE USE TO APP NAME TO SHOE LOGGER
    logger.debug("This is another info message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
    return HttpResponse("Home Page")
