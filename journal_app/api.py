from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)


@router.get("/students/", response_model=List[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    students = crud.get_students(db)
    return students


@router.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.patch("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    updated_student = crud.update_student(db, student_id, student)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student


@router.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = crud.delete_student(db, student_id)
    if deleted_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return deleted_student


@router.post("/scores/", response_model=schemas.Score)
def create_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    return crud.create_score(db=db, score=score)


@router.get("/scores/", response_model=List[schemas.Score])
def read_scores(db: Session = Depends(get_db)):
    scores = crud.get_scores(db)
    return scores


@router.get("/scores/{score_id}", response_model=schemas.Score)
def read_score(score_id: int, db: Session = Depends(get_db)):
    score = crud.get_score(db, score_id)
    if score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return score


@router.patch("/scores/{score_id}", response_model=schemas.Score)
def update_score(score_id: int, score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    updated_score = crud.update_score(db, score_id, score)
    if updated_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return updated_score


@router.delete("/scores/{score_id}", response_model=schemas.Score)
def delete_score(score_id: int, db: Session = Depends(get_db)):
    deleted_score = crud.delete_score(db, score_id)
    if deleted_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return deleted_score
