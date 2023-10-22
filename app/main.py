import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from loguru import logger

from db import SessionLocal, engine, Base
from schemas import QuestionScheme
from services import get_new_questions, get_questions

# Создание экземпляра FastAPI
app = FastAPI()


# Подключение к сессси базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/questions/")
def request_questions(questions_num: int, db: Session = Depends(get_db)):
    """
    Роут для создания новых вопросов.
    Возвращает последний вопрос, созданный при предыдущем запросе.
    Если вопроса нет, то возвращает пустой объект.
    """
    logger.info(f"Request {questions_num} questions.")
    db_question = get_new_questions(db, questions_num=questions_num)
    if not db_question:
        return {}
    return QuestionScheme.model_validate(db_question)


@app.get("/questions/")
def read_questions(db: Session = Depends(get_db)):
    """
    Роут для получения всех вопросов в базе данных.
    """
    questions = get_questions(db)
    return questions


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=8000)
