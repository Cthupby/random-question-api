import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from loguru import logger

from db import SessionLocal, engine, Base
from schemas import NumScheme, QuestionScheme
from services import get_new_questions, get_questions

# Создание экземпляра FastAPI
app = FastAPI()


# Подключение к сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/questions/")
def request_questions(num: NumScheme, db: Session = Depends(get_db)):
    """
    Роут для создания новых и получения предыдущих вопросов.
    Необходимо ввести целое число (количество необъодимых вопросов)
    в поле "questions_num": 2.
    Возвращает последний вопрос, созданный при запросе.
    Если вопроса нет, то возвращает пустой объект.
    """
    logger.info(f'Request {num.questions_num} questions.')
    db_question = get_new_questions(db, questions_num=num.questions_num)
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
