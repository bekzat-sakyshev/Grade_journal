from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
import crud


def load_data():
    db = SessionLocal()

    students = [
        schemas.StudentCreate(name="John Doe"),
        schemas.StudentCreate(name="Jane Smith"),
    ]
    for student in students:
        crud.create_student(db=db, student=student)

    db.close()


if __name__ == "__main__":
    load_data()
