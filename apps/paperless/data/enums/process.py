from enum import Enum
from dataclasses import dataclass
from typing import Type
from more_itertools import first


@dataclass
class PaperlessProcessValue:
    id : int
    model_name : str

class PaperlessProcess(Enum):

    GOODS_EXIT = PaperlessProcessValue(id = 1, model_name = 'GoodsExitDoc')


    @classmethod
    def get_process_by_id(cls, id: int) -> 'PaperlessProcess':
       return first([i for i in cls if i.value.id == id])

