from enum import Enum
from dataclasses import dataclass
from typing import Type



@dataclass
class PaperlessProcessValue:
    id : int
    model_name : str

class PaperlessProcess(Enum):

    GOODS_EXIT = PaperlessProcessValue(id = 1, model_name = 'GoodsExitDoc')

