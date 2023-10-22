from pydantic import BaseModel


class QuestionScheme(BaseModel):
    """
    Схема валидации данных модели Вопроса.
    """
    id: int | str
    answer: str | None
    question: str | None
    value: int | str | None
    created_at: str | None
    category_title: str | None

    class Config:
        from_attributes = True
