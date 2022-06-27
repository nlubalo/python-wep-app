from app import app

def test1():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test2():
    response = app.test_client().get('/base')
    assert response.status_code == 200


def test3():
    response = app.test_client().get('/base')
    # b"To Do App" in response.data
    # # assert b"Todo Title" in response.data
    # assert b"Project" in response.data