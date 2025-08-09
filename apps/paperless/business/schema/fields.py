from pydantic import Field, PlainSerializer
from typing import Annotated


to_lower_case = lambda s: s.lower()

UsernameField = Annotated[
    str,
    Field(frozen=True, min_length=4, max_length=32),
    PlainSerializer(to_lower_case, return_type=str, when_used="always"),
]

PasswordField = Annotated[str, Field(frozen=True, min_length=4, max_length=32)]
IdField = Annotated[int, Field(frozen=True, gt=0)]
ShortStringField = Annotated[str, Field(frozen=True, min_length=1, max_length=64)]
StringField = Annotated[str, Field(frozen=True, min_length=1, max_length=512)]
PositiveShortIntField = Annotated[int, Field(frozen=True, gt=0, lt=65536)]
BooleanField = Annotated[bool, Field(frozen=True)]
