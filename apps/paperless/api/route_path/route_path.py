from dataclasses import dataclass
from typing import ClassVar


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
            raise ValueError("Scope cannot contain underscore")

    @property
    def url(self) -> str:
        return f'/{self.version}/{self.scope}/{self.path}'

    def __repr__(self):
        return self.url

    def __str__(self):
        return self.url


class Routes:

    class User:
        create : ClassVar[ApiRoute] = ApiRoute(scope='user', path='create')
        read_one : ClassVar[ApiRoute] = ApiRoute(scope='user', path='read-one')
        read_many : ClassVar[ApiRoute] = ApiRoute(scope='user', path='read-many')
        update : ClassVar[ApiRoute] = ApiRoute(scope='user', path='update')
        delete : ClassVar[ApiRoute] = ApiRoute(scope='user', path='delete')

    class Auth:
        login : ClassVar[ApiRoute] = ApiRoute(scope='auth', path='login')
        change_password : ClassVar[ApiRoute] = ApiRoute(scope='auth', path='change_password')
        reset_password : ClassVar[ApiRoute] = ApiRoute(scope='auth', path='reset_password')

    class GoodsExit:
        create : ClassVar[ApiRoute] = ApiRoute(scope='goods-exit', path='create')
        read_one : ClassVar[ApiRoute] = ApiRoute(scope='goods-exit', path='read-one')
        read_many : ClassVar[ApiRoute] = ApiRoute(scope='goods-exit', path='read-many')
        update : ClassVar[ApiRoute] = ApiRoute(scope='goods-exit', path='update')
        delete : ClassVar[ApiRoute] = ApiRoute(scope='goods-exit', path='delete')



