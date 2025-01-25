import datetime
import uuid
from sqlalchemy import text
from crm_app.database import async_engine
from crm_app.models.models import metadata


async def create_tables(async_engine):
    # Работаем с синхронными методами через run_sync
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)  # Удаляем таблицы
        await conn.run_sync(metadata.create_all)  # Создаем таблицы


async def insert_data(
        name: str, 
        phone: str, 
        email: str, 
        city: str, 
        region: str, 
        address: str
):
    async with async_engine.connect() as conn:
        async with conn.begin():
            idnumb = str(uuid.uuid4())
            timestamp = datetime.datetime.now(datetime.timezone.utc)
            sql = """INSERT INTO clients (id, name, phone, email, city, region, address, create_on, updated_on) VALUES (:id, :name, :tel, :email, :city, :region, :address, :create_on, :updated_on) returning *;"""
            res = await conn.execute(
                text(sql), {
                'id': idnumb, 
                'name': name, 
                'tel': phone, 
                'email': email,
                'city': city,
                'region': region,
                'address': address,
                'create_on': timestamp,
                'updated_on': timestamp,
                }
            )
            p1 = res.fetchone()
            return p1
        

async def select_clients():
    async with async_engine.connect() as conn:
        sql = text("SELECT * FROM clients;")
        res = await conn.execute(sql)
        clients = res.fetchall()
        return clients
    

async def select_client(client_id: str):
    async with async_engine.connect() as conn:
        sql = """SELECT * FROM clients WHERE clients.id = :client_id"""
        res = await conn.execute(text(sql), {"client_id": client_id})
        p1 = res.fetchone()  # Получение первой записи как словаря
        return p1
    

async def insert_note(note, client_id):
    async with async_engine.connect() as conn:
        async with conn.begin():
            idnumb = str(uuid.uuid4())
            sql = """INSERT INTO notes (id, note, client_id) VALUES (:id, :note, :client_id) returning *;"""
            res = await conn.execute(text(sql), {
                'id': idnumb,
                'note': note,
                'client_id': client_id,
            })
            p1 = res.fetchone()
            return p1


async def select_notes():
    async with async_engine.connect() as conn:
        sql = "SELECT * FROM notes;"
        res = await conn.execute(text(sql))
        notes = res.fetchall()
        return notes
    

async def select_note(note_id: str):
    async with async_engine.connect() as conn:
        sql = """SELECT * FROM notes WHERE notes.id = :note_id"""
        res = await conn.execute(text(sql), {"note_id": note_id})
        p1 = res.fetchone()  # Получение первой записи как словаря
        return p1
    

async def select_clients_notes(client_id: str):
    async with async_engine.connect() as conn:
        sql = """SELECT * FROM notes WHERE notes.client_id = :client_id"""
        res = await conn.execute(text(sql), {"client_id": client_id})
        notes = res.fetchall()  # вернет все заметки
        return notes
    

async def insert_notification(notification, date, client_id):
    async with async_engine.connect() as conn:
        async with conn.begin():
            idnumb = str(uuid.uuid4())
            timestamp = datetime.datetime.now(datetime.timezone.utc)
            sql = """INSERT INTO notifications (id, notification, date, client_id, create_on) VALUES (:id, :notification, :date, :client_id, :create_on) returning *;"""
            res = await conn.execute(text(sql), {
                'id': idnumb,
                'notification': notification,
                'date': date,
                'client_id': client_id,
                'create_on': timestamp,
                }
            )
            p1 = res.fetchone()
            return p1
        
async def select_notifications():
    async with async_engine.connect() as conn:
        sql = """SELECT * FROM notifications"""
        res = await conn.execute(text(sql))
        p1 = res.fetchall()  # Получение первой записи как словаря
        return p1