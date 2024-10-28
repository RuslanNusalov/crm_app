import uuid
from fastapi.testclient import TestClient
from src.crm_app.main import app


# Инициализация клиента для тестирования FastAPI
client = TestClient(app)

# Пример мокированных данных для клиента
mock_client_data = {
    "id": str(uuid.uuid4()),
    "name": "John Doe",
    "phone": "+1234567890",
    "email": "johndoe@example.com",
    "city": "Test City",
    "region": "Test Region",
    "address": "123 Test St",
    "create_on": "2023-09-25T14:48:00",
    "updated_on": "2023-09-25T14:48:00"
}


# Тест успешного получения клиента
def test_get_client_success(mocker):
    # Мокаем функцию select_client, чтобы она возвращала данные клиента
    mocker.patch('crm_app.main.select_client', return_value=mock_client_data)

    # Генерируем URL с мокированным client_id
    client_id = mock_client_data["id"]
    response = client.get(f"/clients/{client_id}")

    # Проверяем, что статус-код 200
    assert response.status_code == 200

    # Проверяем, что возвращаемые данные соответствуют ожидаемым
    assert response.json() == mock_client_data


# Тест, когда клиент не найден (должно быть выброшено исключение HTTPException)
def test_get_client_not_found(mocker):
    # Мокаем функцию select_client, чтобы она возвращала None (клиент не найден)
    mocker.patch('crm_app.core.select_client', return_value=None)

    # Генерируем случайный UUID для несуществующего клиента
    client_id = str(uuid.uuid4())
    response = client.get(f"/clients/{client_id}")
    
    # Проверяем, что статус-код 404
    assert response.status_code == 404

    # Проверяем сообщение об ошибке
    assert response.json() == {"detail": "Client not found"}

