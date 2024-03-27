"""App Configuration"""

# Django
from django.apps import AppConfig

# AA srppayouts App
from srppayouts import __version__


class srppayoutsConfig(AppConfig):
    """App Config"""

    name = "srppayouts"
    label = "srppayouts"
    verbose_name = f"srppayouts App v{__version__}"
