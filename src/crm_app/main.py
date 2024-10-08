import datetime
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from crm_app.core import insert_data, select_data, select_client

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
    

# Endpoint to create a new client
@app.post("/clients", response_model=ClientCreate)
async def create_client(client: ClientCreate) -> Client:
    new_client = await insert_data(**dict(client))
    return new_client


@app.get("/clients/all/") 
async def get_clients() -> Client:
    clients = await select_data()
    if not clients:
        raise HTTPException(status_code=404, detail="Clients not found")
    return clients

@app.get("/clients/{client_id}")
async def get_client(client_id: str) -> Client:
    client = await select_client(client_id)
    print(client)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# # Endpoint to get notes with pagination
# @app.get("/notes", response_model=List[NoteRead])
# def get_notes(limit: int = 10, offset: int = 0, db: Session = None):
#     notes_list = db.query(notes).offset(offset).limit(limit).all()
#     return notes_list

# # Endpoint to add a new note
# @app.post("/notes", response_model=NoteRead)
# def add_note(note: NoteCreate, db: Session = None):
#     new_note = notes(**note.model_dump())
#     db.add(new_note)
#     db.commit()
#     db.refresh(new_note)
#     return new_note



# Initialize database and create tables
# create_tables()
# Uncomment the following line if you want to insert some initial data
# insert_data()
