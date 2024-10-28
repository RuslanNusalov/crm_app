import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from src.crm_app.main import app


@pytest.mark.asyncio
async def test_get_note_success(mocker):
    # Подменим функцию select_note, чтобы она возвращала тестовые данные
    mock_note = {
        "id": "test-note-id",
        "note": "Test Note",
        "client_id": "This is a test client"
    }
    mocker.patch("main.get_note", return_value=mock_note)

    # Используем AsyncClient для асинхронных запросов
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/notes/test-note-id")
    
    assert response.status_code == 200
    assert response.json() == mock_note

@pytest.mark.asyncio
async def test_get_note_not_found(mocker):
    # Подменим функцию select_note, чтобы она возвращала None
    mocker.patch("main.get_note", return_value=None)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/notes/nonexistent-id")

    assert response.status_code == 404
    assert response.json() == {"detail": "Note not found"}