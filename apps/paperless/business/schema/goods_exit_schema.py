from pydantic import ConfigDict, BaseModel

class GoodsExitBase(BaseModel):
    description: str
    sap_code: str
    count: int
    unit_of_measure_id: int
    goods_exit_doc_id: int

class GoodsExitCreate(GoodsExitBase):
    pass

class GoodsExitUpdate(BaseModel):
    description: str | None = None
    sap_code: str | None = None
    count: int | None = None
    unit_of_measure_id: int | None = None
    goods_exit_doc_id: int | None = None

class GoodsExitRead(GoodsExitBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
