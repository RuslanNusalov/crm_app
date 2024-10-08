import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
from crm_app.main import app


# Подключаем TestClient для взаимодействия с FastAPI
client = TestClient(app)


@pytest.mark.asyncio
async def test_get_clients_success(mocker):
    """Тест успешного получения всех клиентов."""

    # Мокируем функцию select_data, чтобы она вернула список клиентов
    mock_clients = [
        {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "name": "John Doe",
            "phone": "+1234567890",
            "email": "johndoe@example.com",
            "city": "New York",
            "region": "NY",
            "address": "123 Main St",
            "create_on": "2024-09-25T12:34:56",
            "updated_on": "2024-09-26T14:34:56"
        }
    ]
    
    # Мокируем вызов select_data через pytest-mock
    mocker.patch('crm_app.main.select_data', new=AsyncMock(return_value=mock_clients))

    # Вызов get-запроса к API
    response = await client.get("/clients/all/")
    
    # Проверка, что статус ответа 200 OK
    assert response.status_code == 200
    # Проверка, что данные возвращаются корректно
    assert response.json() == mock_clients


@pytest.mark.asyncio
async def test_get_clients_not_found(mocker):
    """Тест случая, когда клиенты не найдены."""

    # Мокируем функцию select_data, чтобы она вернула пустой список
    mocker.patch('crm_app.main.select_data', new=AsyncMock(return_value=[]))

    # Вызов get-запроса к API
    response = await client.get("/clients/all/")
    
    # Проверка, что статус ответа 404
    assert response.status_code == 404
    # Проверка, что возвращено правильное сообщение об ошибке
    assert response.json() == {"detail": "Clients not found"}