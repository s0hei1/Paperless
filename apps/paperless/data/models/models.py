from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime,UTC

from apps.paperless.data.enums.approval_status import ApprovalStatus
from apps.paperless.data.enums.process import PaperlessProcess
from apps.paperless.data.enums.user_rolls import UserRoll

SQLAlchemyModel = declarative_base()

class Departments(SQLAlchemyModel):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    code = Column(Integer, nullable=False)

    users = relationship('User', back_populates='department')

class User(SQLAlchemyModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    user_name = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    user_roll = Column(Enum(UserRoll), nullable=False, default=UserRoll.PERSONNEL.value)

    department_id = Column(ForeignKey('departments.id'), nullable=False)

    department = relationship('Departments', back_populates='users')
    approvals = relationship('ApprovalUser', back_populates='user' )
    goods_exit_approvals = relationship("GoodsExitApproval", back_populates="user")

class ApprovalUser(SQLAlchemyModel):
    __tablename__ = 'approval_users'
    id = Column(Integer, primary_key=True)
    approval_process = Column(Enum(PaperlessProcess), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='approvals')

class GoodsExitApproval(SQLAlchemyModel):
    __tablename__ = 'approvals'
    id = Column(Integer, primary_key=True)
    status = Column(Enum(ApprovalStatus), nullable=False)

    user_id = Column(ForeignKey('users.id'), nullable=False)
    doc_id = Column(ForeignKey('goods_exit_docs.id'), nullable=False)

    user = relationship('User', back_populates='goods_exit_approvals')
    doc = relationship('GoodsExitDoc', back_populates='approval')

class GoodsExitDoc(SQLAlchemyModel):
    __tablename__ = "goods_exit_docs"
    id = Column(Integer, primary_key=True)
    doc_code = Column(String(128), nullable=False, unique=True)
    creation_date_time = Column(DateTime, default= datetime.now(UTC))

    sending_department_id  = Column(ForeignKey('departments.id'))
    sending_department_name  = Column(String(128), nullable=False)
    exit_reason  = Column(String(256), nullable=True)
    destination  = Column(String(128), nullable=True)
    address  = Column(String(512), nullable=True)
    sending_user_fullname = Column(String(128), nullable=True)


    sending_department = relationship("Department")
    items = relationship("GoodsExit", back_populates="goods_exit_doc")
    approval = relationship('GoodsExitApproval', back_populates='doc')

class GoodsExit(SQLAlchemyModel):
    __tablename__ = "goods_exits"
    id = Column(Integer, primary_key=True)
    description = Column(String(256), nullable=False)
    sap_code = Column(String(16), nullable=False)
    count = Column(Integer, nullable=False)
    unit_of_measure_id = Column(ForeignKey('unit_of_measures.id'), nullable=False)
    goods_exit_doc_id = Column(ForeignKey('goods_exit_docs.id'), nullable=False)

    unit_of_measure = relationship('UnitOfMeasure')
    goods_exit_doc = relationship('GoodsExitDoc', back_populates='items')

class UnitOfMeasure(SQLAlchemyModel):
    __tablename__ = 'unit_of_measures'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    name_alias = Column(String(64), nullable=True)
