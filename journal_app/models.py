from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    scores = relationship("Score", back_populates="student", cascade="all, delete")


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="scores")
