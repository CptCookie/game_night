from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "game_night.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import game_night.users.signals  # noqa F401
        except ImportError:
            pass
