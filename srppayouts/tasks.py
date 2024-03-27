"""App Tasks"""

# Standard Library
import logging

# Third Party
from celery import shared_task

logger = logging.getLogger(__name__)

# Create your tasks here


# srppayouts Task
@shared_task
def srppayouts_task():
    """srppayouts Task"""

    pass
