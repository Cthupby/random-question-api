def test_questions(test_app):
    response = test_app.get("/questions/")
    assert response.status_code == 200
