from pydantic import BaseModel


class OnAddGoodsExitDocSchema(BaseModel):
    doc_id: int
    department_manager_id: int
    approver_guard_id: int
    approver_manager_id: int

    def get_approvers(self) -> list[int]:
        return self.model_dump(
            include={
                "department_manager_id",
                "approver_guard_id",
                "approver_manager_id",
            }
        )
