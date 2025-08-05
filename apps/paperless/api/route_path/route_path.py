from dataclasses import dataclass
from typing import ClassVar
from abc import ABC

@dataclass()
class ApiRoute:
    scope : str
    path : str
    version : str = 'v1'

    def __post_init__(self):
        self.scope = self.scope.replace('\\', '').replace('/', '')
        self.path = self.path.replace('\\', '').replace('/', '')

        if '_' in self.path:
            raise ValueError("Path cannot contain underscore")
        if '_' in self.scope:
            raise ValueError("Scope cannot contain underscore, check you define scope name for all scopes")

    @property
    def url(self) -> str:
        return f'/{self.version}/{self.scope}/{self.path}'

    def __repr__(self):
        return self.url

    def __str__(self):
        return self.url


class BaseScope(ABC):

    scope_name : str = "_"


class Routes:

    class User(BaseScope):

        scope_name = "user"

        create : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='create')
        read_one : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='read-one')
        read_many : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='read-many')
        update : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='update')
        delete : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='delete')


    class Auth(BaseScope):

        scope_name = "auth"

        login : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='login')
        change_password : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='change-password')
        reset_password : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='reset-password')

    class GoodsExit(BaseScope):
        scope_name = "goods-exit"
        create : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='create')
        read_one : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='read-one')
        read_many : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='read-many')
        update : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='update')
        delete : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='delete')

    class Department(BaseScope):
        scope_name = "department"
        create: ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='create')
        read_one: ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='read-one')
        read_many: ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='read-many')
        update: ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='update')
        delete: ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='delete')

    class GoodsExitDoc(BaseScope):
        scope_name = "goods-exit-doc"
        create : ClassVar[ApiRoute] = ApiRoute(scope=scope_name, path='create')




