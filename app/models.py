from sqlalchemy import Column, Integer, Text

from db import Base


class Question(Base):
    """
    Модель Вопроса.
    Колонки соответсвуют основным полям вопроса из API.
    """
    __tablename__ = "questions"

    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True,
        index=True,
    )
    answer = Column(Text)
    question = Column(Text)
    value = Column(Integer)
    created_at = Column(Text)
    category_title = Column(Text)
