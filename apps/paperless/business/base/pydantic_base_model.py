from pydantic import BaseModel
from apps.paperless.data.value.tvalue import TValue


class Model(BaseModel):

    def to_t_value_dict(self, exclude_unset=True) -> dict[str, TValue]:
        input_fields = self.model_dump(exclude_unset=exclude_unset)

        for i in input_fields:
            input_fields[i] = TValue(input_fields[i])

        return input_fields
