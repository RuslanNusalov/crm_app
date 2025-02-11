import datetime
from typing import List
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from crm_app.core import insert_data, select_clients, select_client, \
    insert_note, select_clients_notes, select_notes, select_note, \
    insert_notification, select_notifications

# from aiogram import Bot
# from bot_notifications import send_notification



app = FastAPI(
    title="CRM App"
)


class ClientCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr
    city: str
    region: str
    address: str


class Client(ClientCreate):
    '''Describes the client model used in the CRM.'''
    id: uuid.UUID
    create_on: datetime.datetime
    updated_on: datetime.datetime
    # is_active: bool


class NoteCreate(BaseModel):
    note: str
    

class Note(NoteCreate):
    '''Describes the notes model used in the CRM.'''
    id: uuid.UUID
    client_id: uuid.UUID | None


class NotificationCreate(BaseModel):
    notification: str
    date: datetime.datetime
    

class Notification(NotificationCreate):
    '''Describes the notes model used in the CRM.'''
    id: uuid.UUID
    client_id: uuid.UUID | None


@app.get("/")
async def root():
    return {"message": "CRM App"}


# Endpoint to create a new client.
@app.post("/clients", response_model=ClientCreate)
async def create_client(client: ClientCreate) -> Client:
    new_client = await insert_data(**dict(client))
    return new_client


# Endpoint to select all clients.
@app.get("/clients", response_model=List[Client])
async def get_clients() -> List[Client]:
    clients = await select_clients()
    if not clients:
        raise HTTPException(status_code=404, detail="Clients not found")
    return clients


# Endpoint to select one client.
@app.get("/clients/{client_id}")
async def get_client(client_id: str) -> Client:
    client = await select_client(client_id)
    print(client)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# Endpoint to select client's notes.
@app.get("/client-notes/{client_id}", response_model=List[Note])
async def get_client_notes(client_id: str):
    notes = await select_clients_notes(client_id)
    print(notes)
    if not notes:
        raise HTTPException(status_code=404, detail="Client's notes not found")
    return notes


# Endpoint to add a new note.
@app.post("/notes", response_model=NoteCreate)
async def create_note(note: NoteCreate, client_id: str) -> Note:
    note_data = note.model_dump()  # Преобразуем объект note в словарь
    new_note = await insert_note(**note_data, client_id=client_id)  # Передаем словарь и client_id
    return new_note


@app.get("/notes", response_model=List[Note])
async def get_notes() -> List[Note]:
    notes = await select_notes()
    if not notes:
        raise HTTPException(status_code=404, detail="Notes not found")
    return notes


# Endpoint to select one client.
@app.get("/notes/{notes_id}")
async def get_note(note_id: str):
    note = await select_note(note_id)
    print(note)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


# Endpoint to add a new notification.
@app.post("/notifications", response_model=NotificationCreate)
async def create_notification(notifcation: NotificationCreate, client_id: str) -> Notification:
    notification_data = notifcation.model_dump()  # Преобразуем объект notification в словарь
    new_notification = await insert_notification(**notification_data, client_id=client_id)  # Передаем словарь и client_id
    return new_notification


@app.get("/notifications", response_model=List[Notification])
async def get_notifications() -> List[Notification]:
    notifications = await select_notifications()
    if not notifications:
        raise HTTPException(status_code=404, detail="notifications not found")
    return notifications


# @app.get("/trigger-notification/")
# async def trigger_notification(background_tasks: BackgroundTasks):
#     """ Триггер для уведомления."""
#     message = "Уведомление: выполнить новую задачу!"
#     background_tasks.add_task(send_notification, message)
#     return {"status": "Уведомление отправлено"}