from fastapi.openapi.models import Schema

from apps.paperless.business.schema.fields import IdField


class DeleteSchema(Schema):
    id : IdField
    message : str = "Delete was successful"