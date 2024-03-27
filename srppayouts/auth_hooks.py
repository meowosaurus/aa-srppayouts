"""Hook into Alliance Auth"""

# Django
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# AA srppayouts App
from srppayouts import urls


class srppayoutsMenuItem(MenuItemHook):
    """This class ensures only authorized users will see the menu entry"""

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _("SRP Payouts"),
            "fas fa-hand-holding-usd fa-fw",
            "srppayouts:index",
            navactive=["srppayouts:"],
        )

    def render(self, request):
        """Render the menu item"""

        if request.user.has_perm("srppayouts.basic_access"):
            return MenuItemHook.render(self, request)

        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """Register the menu item"""

    return srppayoutsMenuItem()


@hooks.register("url_hook")
def register_urls():
    """Register app urls"""

    return UrlHook(urls, "srppayouts", r"^srp-payouts/")
