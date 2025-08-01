from pydantic import Field
from typing import Annotated

UsernameField = Annotated[str, Field(frozen=True,min_length=4, max_length=32)]
PasswordField = Annotated[str,Field(frozen=True,min_length=4, max_length=32)]


