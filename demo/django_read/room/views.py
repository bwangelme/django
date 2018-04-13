import logging
from django.http import HttpResponse
from django.conf import settings

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    if settings.DEBUG:
        logger.debug("In the index view")
    return HttpResponse("Hello")
