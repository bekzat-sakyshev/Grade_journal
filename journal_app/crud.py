from sqlalchemy.orm import Session

import models
import schemas


def get_scores_by_student(db: Session, student_id: int):
    return db.query(models.Score).filter(models.Score.student_id == student_id).all()


def search_students_by_name(db: Session, name: str):
    return db.query(models.Student).filter(models.Student.name.ilike(f"%{name}%")).all()


def get_students(db: Session):
    return db.query(models.Student).all()


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student_id: int, updated_data: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        for key, value in updated_data.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student


def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student


def get_scores(db: Session):
    return db.query(models.Score).all()


def get_score(db: Session, score_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id).first()


def create_score(db: Session, score: schemas.ScoreCreate):
    db_score = models.Score(**score.dict())
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score


def update_score(db: Session, score_id: int, updated_data: schemas.ScoreCreate):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    if db_score:
        for key, value in updated_data.dict().items():
            setattr(db_score, key, value)
        db.commit()
        db.refresh(db_score)
    return db_score


def delete_score(db: Session, score_id: int):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score
