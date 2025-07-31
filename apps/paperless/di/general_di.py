from apps.paperless.config import Settings


class GeneralDI:

    @classmethod
    def settings(cls):
        return Settings()
