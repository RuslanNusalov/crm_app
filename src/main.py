import datetime
from typing import List
import uuid
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from sqlalchemy import TIMESTAMP
from core import create_tables


app = FastAPI(
    title="Crm App"
)


class Client(BaseModel):
    '''Описывает модель клиента, который заносится в CRM.'''
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
    # is_active: bool


# @app.get("/clients/{client_id}", response_model=List[Client])
# def get_client(client_id: int):
#     return [client for client in clients if client.get("id") == client_id]


# @app.get("/notes")
# def get_notes(limit: int = 10, offset: int = 0):
#     return notes[offset:][:limit]


class Note(BaseModel):
    '''Описывает модель заметки по клиенту.'''
    id: uuid
    client_id: int
    text: str


@app.post("/notes")
def add_note(notes: List[Note]):
    notes.extend(notes)
    return {"status": 200, "data": notes}


# @app.post("/clients")
# def add_clients(clients: List[Client]):
#      notes.extend(clients)
#      return {"status": 200, "data": clients}


create_tables()
