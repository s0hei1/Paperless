from sqlalchemy import (
    Column,
    Integer,
    String,
    Enum,
    ForeignKey,
    DateTime,
    Boolean,
)
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from datetime import datetime, UTC
from apps.paperless.data.enums.approval_status import ApprovalStatus
from apps.paperless.data.enums.unit_of_measure import UOMs
from apps.paperless.data.enums.user_rolls import UserRoll


class SQLAlchemyModel(DeclarativeBase):
    pass


class Department(SQLAlchemyModel):
    __tablename__ = "departments"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), unique=True)
    code: Mapped[int] = mapped_column(unique=True)
    manager_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", use_alter=True))

    users = relationship(
        "User", back_populates="department", foreign_keys="User.department_id"
    )
    manager_user = relationship(
        "User", back_populates="managed_department", foreign_keys=[manager_id]
    )


class User(SQLAlchemyModel):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    user_name: Mapped[str] = mapped_column(String(32), unique=True)
    password: Mapped[str] = mapped_column(String(32))
    user_roll : Mapped[UserRoll] = mapped_column(default=UserRoll.PERSONNEL)

    department_id : Mapped[int]= mapped_column(ForeignKey("departments.id"), nullable=False)

    department = relationship(
        "Department",
        back_populates="users",
        foreign_keys=[department_id],
    )
    managed_department = relationship(
        "Department",
        back_populates="manager_user",
        foreign_keys="Department.manager_id",
    )
    goods_exit_approvals = relationship("GoodsExitApproval", back_populates="user")


class GoodsExitApproval(SQLAlchemyModel):
    __tablename__ = "approvals"
    id : Mapped[int] = mapped_column(primary_key=True)
    status : Mapped[ApprovalStatus]
    user_id : Mapped[int]= mapped_column(ForeignKey("users.id"))
    doc_id : Mapped[int]= mapped_column(ForeignKey("goods_exit_docs.id"))
    modification_date_time : Mapped[datetime]= mapped_column(default=datetime.now(UTC))
    user = relationship("User", back_populates="goods_exit_approvals")
    doc = relationship("GoodsExitDoc", back_populates="approvals")


class GoodsExitDoc(SQLAlchemyModel):
    __tablename__ = "goods_exit_docs"
    id : Mapped[int ]= mapped_column(primary_key=True)
    doc_code : Mapped[str]= mapped_column(String(8), unique=True)
    creation_date_time : Mapped[datetime]= mapped_column(default=datetime.now(UTC))
    sending_department_id : Mapped[int] = mapped_column(ForeignKey("departments.id"))
    sending_department_name : Mapped[str] = mapped_column(String(128))
    exit_reason : Mapped[str] = mapped_column(String(256))
    destination : Mapped[str] = mapped_column(String(128))
    address_ : Mapped[str] = mapped_column(String(512))
    sending_user_fullname : Mapped[str] = mapped_column(String(128))
    exit_for_ever : Mapped[bool]
    receiver_name : Mapped[str | None] = mapped_column(String(128))
    status : Mapped[ApprovalStatus]
    approval_status : Mapped[ApprovalStatus]
    creator_user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))

    approvals = relationship("GoodsExitApproval", back_populates="doc")
    creator_user = relationship("User", backref="goods_exit_docs")
    sending_department = relationship("Department")
    items = relationship("GoodsExit", back_populates="goods_exit_doc")


class GoodsExit(SQLAlchemyModel):
    __tablename__ = "goods_exits"
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    description : Mapped[str]= mapped_column(String(256))
    sap_code : Mapped[str | None]= mapped_column(String(16))
    count : Mapped[int]
    unit_of_measure : Mapped[UOMs]
    goods_exit_doc_id : Mapped[int] = mapped_column(ForeignKey("goods_exit_docs.id"))

    goods_exit_doc = relationship("GoodsExitDoc", back_populates="items")
