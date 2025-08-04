from fastapi import Depends

from apps.paperless.business.service.auth_service import AuthService
from apps.paperless.data.db.db import get_read_only_db
from apps.paperless.di import GeneralDI


class ServiceDI():

    @classmethod
    def auth_service(cls, db = Depends(get_read_only_db)):
        return AuthService(db=db)