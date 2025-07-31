from enum import Enum

from dataclasses import dataclass
from typing import Type
from apps.paperless.data.models.models import GoodsExitDoc


@dataclass
class PaperlessProcessValue:
    id : int
    model_name : Type

class PaperlessProcess(Enum):
    GOODS_EXIT = PaperlessProcessValue(id = 1, model_name = GoodsExitDoc)

