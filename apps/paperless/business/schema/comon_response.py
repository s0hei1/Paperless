from fastapi.openapi.models import Schema
from pydantic import ConfigDict

from apps.paperless.business.schema.fields import IdField


class DeleteSchema(Schema):
    id : IdField
    message : str = "Delete was successful"

    model_config = ConfigDict(from_attributes= True)