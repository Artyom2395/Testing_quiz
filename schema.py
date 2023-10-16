from pydantic import BaseModel

class QuestionCreate(BaseModel):
    questions_num: int