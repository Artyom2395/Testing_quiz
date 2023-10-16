from sqlalchemy.orm import Session
from models import Question

def get_latest_question(db: Session):
    return db.query(Question).order_by(Question.id.desc()).first()

def create_question(db: Session, question_data: dict):
    question = Question(**question_data)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question