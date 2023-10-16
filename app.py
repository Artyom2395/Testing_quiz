import httpx

from fastapi import FastAPI, HTTPException

from models import Question, Base
from schema import QuestionCreate
from database import SessionLocal, engine
from crud import get_latest_question, create_question

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/questions/")
async def create_questions(questions_data: QuestionCreate):
    if questions_data.questions_num <= 0:
        raise HTTPException(status_code=400, detail="Invalid number of questions")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jservice.io/api/random?count={questions_data.questions_num}")
        items = response.json()

    with SessionLocal() as db:
        existing_question = get_latest_question(db)

        for item in items:
            question_data = {
                "question": item["question"],
                "answer": item["answer"],
                "created_at": item["created_at"]
            }

            # Проверка уникальности вопроса
            if existing_question and existing_question.question == question_data["question"]:
                continue

            create_question(db, question_data)
            existing_question = db.query(Question).order_by(Question.id.desc()).first()

        return existing_question.question