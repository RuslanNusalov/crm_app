import pytest
from httpx import AsyncClient
from src.crm_app.main import app


@pytest.mark.asyncio
async def test_create_note():
    # Данные для создания новой заметки
    note_data = {
        "title": "Test Note",
        "content": "This is a test note",
    }

    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Отправка POST запроса для создания заметки
        response = await ac.post("/notes", json=note_data)

    # Проверяем, что запрос прошел успешно
    assert response.status_code == 200

    # Проверяем, что возвращенные данные соответствуют ожиданиям
    response_json = response.json()
    assert response_json["title"] == note_data["title"]
    assert response_json["content"] == note_data["content"]