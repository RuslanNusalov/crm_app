import pytest
from httpx import AsyncClient
from fastapi import FastAPI, HTTPException
from src.crm_app.main import app, get_notes  # здесь функция, которая получает записи


# Создаем моки для функции select_notes
@pytest.fixture
def mock_select_notes(monkeypatch):
    async def mock_notes_found():
        return [{"id": 1, "content": "Test Note"}]  # возвращаем некий список заметок
    
    async def mock_notes_not_found():
        return []  # пустой список означает, что заметки не найдены
    
    # Фикстура возвращает обе функции для использования в тестах
    return mock_notes_found, mock_notes_not_found


@pytest.mark.asyncio
async def test_get_notes_success(mock_select_notes):
    mock_notes_found, _ = mock_select_notes
    # Патчим функцию select_notes, чтобы она возвращала заранее подготовленные данные
    monkeypatch.setattr("crm_app.main.get_notes", mock_notes_found)
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/notes/all/")
    
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "content": "Test Note"}]  # Проверяем корректность ответа


@pytest.mark.asyncio
async def test_get_notes_not_found(mock_select_notes):
    _, mock_notes_not_found = mock_select_notes
    monkeypatch.setattr("crm_app.main.get_notes", mock_notes_not_found)
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/notes/all/")
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Notes not found"}  # Проверяем сообщение об ошибке