import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
from crm_app.main import app



client = TestClient(app)

@pytest.mark.asyncio
async def test_create_client(mocker):
    # Подготавливаем тестовые данные
    client_data = {
        "name": "Test Client",
        "phone": "+123456789",
        "email": "test@example.com",
        "city": "Test City",
        "region": "Test Region",
        "address": "Test Address"
    }
    
    # Мокаем insert_data, чтобы не обращаться к настоящей БД
    mock_insert = mocker.patch('crm_app.core.insert_data', new=AsyncMock(return_value=client_data))
    
    # Выполняем POST запрос к эндпоинту
    response = await client.post("/clients", json=client_data)
    
    # Проверяем успешный статус код
    assert response.status_code == 200
    
    # Проверяем, что функция insert_data была вызвана с правильными аргументами
    mock_insert.assert_called_once_with(**client_data)
    
    # Проверяем, что ответ соответствует ожидаемому
    assert response.json() == client_data