# -- coding: utf-8 --

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    VARCHAR,
    Date,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .meta import Base

class Proposal(Base):

    __tablename__ = "Proposal"
    id = Column(Integer,primary_key= True)
    year = Column(Date)#ปีการศึกษา
    location = Column(Text)#สถานที่
    working_location = Column(Text)#สถานที่จัดกิจกรรม/สถานที่ดำเนินงาน/สถานที่ปฏิบัติงาน
    Reason = Column(Text)#หลักการ และเหตุผล

    objective = relationship("Objective", back_populates = "parent_proposal")#วัตถุประสงค์

    activity_comparition = Column(Text)
    number_of_member = Column(Integer)
    evaluation_index = Column(Text)#รูปแบบการประเมินผล
    profit = Column(Text)#ประโบชน์ที่คาดว่าจะได้รับ/ผลที่คาดว่าจะได้รับ
    type_of_activity = Column(Text)#ลักษณะกิจกรรม/ลักษณะการปฏิบัติงาน

    cost = relationship("Cost",back_propulates="parent_proposal")#ค่าใช้จ่ายในการจัดกิจกรรม

    success_criteria = Column(Text)#ตัวชี้วัดความสำเร็จของโครงการ
    previouse_result = relationship("Previouse_result",back_populates = "parent_proposal")#ผลการจัดที่ผ่านมา

    parent_project = relationship("Project", back_populates = "proposal", uselist = False)




class Objective(Base):
    __tablename__ = "Objective"
    id = Column(Integer , primary_key=True)
    text = Column(Text)

    proposal_id = Column(Integer,ForeignKey("Proposal.id"))
    parent_proposal = relationship("Proposal", back_populates="objective")

class Cost(Base):
    __tablename__ = "Cost"
    id = Column(Integer,primary_key=True)
    text  =Column(Text)

    proposal_id = Column(Integer,ForeignKey("Proposal.id"))
    parent_proposal = relationship("Proposal",back_populates="cost")

class Previouse_result(Base):
    __tablename__ = "Previouse_result"
    id = Column(Integer,primary_key=True)
    text = Column(Text)

    proposal_id = Column(Integer,ForeignKey("Proposal.id"))
    parent_proposal = relationship("Proposal",back_populates = "previouse_result")