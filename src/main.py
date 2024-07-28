import datetime
from typing import List
import uuid
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from sqlalchemy import TIMESTAMP


app = FastAPI(
    title="Crm App"
)


# fake_clients = [
#     {"id": 1, "name": "Bob", "phone_list": [{"id": 1, "phone_number": "765"}], "profession": "менеджер", "create_at": "2021-11-04T00:05:21"},
#     {"id": 2, "name": "John", "phone_list": [{"id": 2, "phone_number": "766"}], "profession": "директор", "create_at": "2021-10-04T00:05:13"},
#     {"id": 3, "name": "vasiliy", "phone_list": [{"id": 3, "phone_number": "767"}], "profession": "фокусник", "create_at": "2022-11-04T00:09:23"},
# ]


# class Phone(BaseModel):
#     id: int
#     phone_number: str


class Client(BaseModel):
    id: uuid
    name: str
    phone: str
    email: EmailStr
    city: str
    region: str
    address: str
    create_on: TIMESTAMP
    updated_on: datetime
    parent_user_id: int
    is_active: bool


@app.get("/clients/{client_id}", response_model=List[Client])
def get_client(client_id: int):
    return [client for client in clients if client.get("id") == client_id]


# fake_notes = [
#     {"id": 1, "client_id": 1, "note": "клиент имеет 3 млн, хочет купить студию в  Сочи"},
#     {"id": 2, "client_id": 2, "note": "клиент имеет 10 млн, хочет купить дом в Краснодаре"},
#     {"id": 3, "client_id": 3, "note": "клиент имеет 5 млн, хочет купить 1 км. квартиру в Краснодаре"},
# ]

@app.get("/notes")
def get_notes(limit: int = 10, offset: int = 0):
    return notes[offset:][:limit]


class Note(BaseModel):
    id: uuid
    client_id: int
    text: str


@app.post("/notes")
def add_note(notes: List[Note]):
    notes.extend(notes)
    return {"status": 200, "data": notes}


@app.post("/clients")
def add_clients(clients: List[Client]):
     notes.extend(clients)
     return {"status": 200, "data": clients}
