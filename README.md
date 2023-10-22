# Random Question API

## Технологии проекта:

* Web: [FastAPI](https://fastapi.tiangolo.com/), [Uvicorn](https://www.uvicorn.org/), [Requests](https://requests.readthedocs.io/en/latest/)
* Database: [PostgreSQL](https://www.postgresql.org/), [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

## Запуск  

### При помощи [docker compose](https://docs.docker.com/compose/)
1. Необходимо скачать репозиторий и перейти в него:  
   ```
   git clone https://github.com/Cthupby/random-question-api.git && cd random-question-api
   ```  
2. Создать Docker образ:  
   ```
   docker build -t random_question_api_image .
   ```  
3. Создать и активировать Docker контейнеры:  
   ```
   docker-compose up -d
   ```  
4. Перейти на локальный адрес и сделать POST запрос через Swagger UI:   
   ```
   http://0.0.0.0:8000/docs
   ```  
   Или, пример, запроса при помощи [curl](https://curl.se/docs/):   
   ```
   curl -X 'POST' \
      'http://0.0.0.0:8000/questions/' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
          "questions_num": 2
      }'
   ```  
   Ответом должно быть:  
   ```
   {}
   ```
   или  
   ```
   
   {
       "id": <id>,
       "answer": <answer>,
       "question": <question>,
       "value": <value>,
       "created_at": <created_at>,
       "category_title": <category_title>
   }
   ```
