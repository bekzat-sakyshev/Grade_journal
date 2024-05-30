from pydantic import BaseModel, Field


class StudentBase(BaseModel):
    name: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True


class ScoreBase(BaseModel):
    value: int
    student_id: int


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int

    class Config:
        orm_mode = True
