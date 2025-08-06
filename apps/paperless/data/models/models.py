from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, UTC
from apps.paperless.data.enums.approval_status import ApprovalStatus
from apps.paperless.data.enums.unit_of_measure import UOMs
from apps.paperless.data.enums.user_rolls import UserRoll

SQLAlchemyModel = declarative_base()

class Department(SQLAlchemyModel):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    code = Column(Integer, nullable=False, unique=True)
    manager_id = Column(ForeignKey('users.id',use_alter=True), nullable=True)

    users = relationship('User', back_populates='department',foreign_keys = 'User.department_id')
    manager_user = relationship('User', back_populates='managed_department',foreign_keys = [manager_id])

class User(SQLAlchemyModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    user_name = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    user_roll = Column(Enum(UserRoll), nullable=False, default=UserRoll.PERSONNEL.value)

    department_id = Column(ForeignKey('departments.id'), nullable=False)

    department = relationship('Department', back_populates='users', foreign_keys=[department_id],)
    managed_department = relationship('Department', back_populates='manager_user', foreign_keys="Department.manager_id")
    goods_exit_approvals = relationship("GoodsExitApproval", back_populates="user")

class GoodsExitApproval(SQLAlchemyModel):
    __tablename__ = 'approvals'
    id = Column(Integer, primary_key=True)
    status = Column(Enum(ApprovalStatus), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    doc_id = Column(ForeignKey('goods_exit_docs.id'), nullable=False)
    modification_date_time = Column(DateTime, default=datetime.now(UTC))
    user = relationship('User', back_populates='goods_exit_approvals')
    doc = relationship('GoodsExitDoc', back_populates='approvals')


class GoodsExitDoc(SQLAlchemyModel):
    __tablename__ = "goods_exit_docs"
    id = Column(Integer, primary_key=True)
    doc_code = Column(String(8), nullable=False, unique=True)
    creation_date_time = Column(DateTime, default=datetime.now(UTC))
    sending_department_id = Column(ForeignKey('departments.id'))
    sending_department_name = Column(String(128), nullable=False)
    exit_reason = Column(String(256), nullable=False)
    destination = Column(String(128), nullable=False)
    address_ = Column(String(512), nullable=False)
    sending_user_fullname = Column(String(128), nullable=False)
    exit_for_ever = Column(Boolean, nullable=False)
    receiver_name = Column(String(128), nullable=True)
    status = Column(Enum(ApprovalStatus), nullable=False)

    approval_status = Column(Enum(ApprovalStatus), nullable=False)
    creator_user_id = Column(ForeignKey('users.id'))

    approvals = relationship('GoodsExitApproval', back_populates='doc')
    creator_user = relationship('User', backref='goods_exit_docs')
    sending_department = relationship("Department")
    items = relationship("GoodsExit", back_populates="goods_exit_doc")

class GoodsExit(SQLAlchemyModel):
    __tablename__ = "goods_exits"
    id = Column(Integer, primary_key=True)
    description = Column(String(256), nullable=False)
    sap_code = Column(String(16), nullable=True)
    count = Column(Integer, nullable=False)
    unit_of_measure = Column(Enum(UOMs), nullable=False)
    goods_exit_doc_id = Column(ForeignKey('goods_exit_docs.id'), nullable=False)

    goods_exit_doc = relationship('GoodsExitDoc', back_populates='items')
