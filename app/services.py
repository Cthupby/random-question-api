import asyncio
import json
import requests

from sqlalchemy.orm import Session
from loguru import logger

from models import Question
from schemas import QuestionScheme


def create_question(db: Session, question: QuestionScheme):
    """
    Функция для создания новых вопросов в базе данных на основании схемы.
    """
    db_question = Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_questions(db: Session):
    """
    Функция для получения всех вопросов в базе данных.
    """
    return db.query(Question).all()


def get_question_by_id(db: Session, question_id: int) -> Question | None:
    """
    Функция для получения вопроса из базы данных по его id.
    Необходима для проверки уникальности вопроса.
    """
    return db.query(Question).filter(Question.id==question_id).first()


def get_last_question(db: Session) -> Question | None:
    """
    Функция для получения последнего вопроса из базы данных.
    """
    return db.query(Question).order_by(Question.id.desc()).first()


def request_new_questions(questions_num: int):
    """
    Функция для получения данных из API.
    """
    headers = {'Accept': 'application/json'}
    new_questions = requests.get(
        f'https://jservice.io/api/random?count={questions_num}',
        headers=headers,
    ).json()
    return new_questions


def get_new_questions(
    db: Session,
    questions_num: int,
) -> Question | None:
    """
    Функция для создания новых вопросов при подключении к API.
    Возвращает последний вопрос из базы данных.
    """
    last_question = get_last_question(db)
    new_questions = request_new_questions(questions_num)
    i = 0
    while i < questions_num:
        """
        Необходимо создать questions_num новых вопросов.
        Для этого проверяем наличие вопроса в базе данных по его id.
        Если вопрос есть в бд, то делаем новый запрос к API.
        """
        new_question_data = new_questions[i]
        question = get_question_by_id(db, new_question_data["id"])
        if not question:
            new_question = create_question(db, QuestionScheme(
                id=new_question_data["id"],
                answer=new_question_data["answer"],
                question=new_question_data["question"],
                value=new_question_data["value"],
                created_at=new_question_data["created_at"],
                category_title=new_question_data["category"]["title"],
            ))
            i += 1
            logger.info(f"Create new question with id: {new_question.id}!")
        else:
            logger.info(f'Question {new_question_data["id"]} already exist!')
            questions_num -= i
            new_questions = request_new_questions(questions_num)
    return last_question

