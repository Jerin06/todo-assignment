from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_todo():
    response = client.post(
        "/todo/create",
        json={"id": "1345", "task": "My first task"},
    )
    assert response.status_code == 200
    assert response.json()["data"] == {
        "id": "1345",
        "task": "My first task",
        "is_done": False,
    }
    
    
def test_get_todo():
    response = client.post(
        "/todo/get",
        json={"id": "1345"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "1345",
        "task": "My first task",
        "is_done": False,
    }
    
    
def test_update_todo():
    response = client.post(
        "/todo/update",
        json={"id": "1345"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "1345",
        "task": "My first task",
        "is_done": True,
    }
    