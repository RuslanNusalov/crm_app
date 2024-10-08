import datetime
import uuid
from sqlalchemy import text
from crm_app.database import async_engine
from crm_app.models.models import metadata


def create_tables():
    async_engine.echo = False
    metadata.drop_all(async_engine)
    metadata.create_all(async_engine)
    async_engine.echo = True


async def insert_data(name, phone, email, city, region, address):
    try:
        async with async_engine.connect() as conn:
            async with conn.begin():
                idnumb = str(uuid.uuid4())
                timestamp = datetime.datetime.utcnow()
                sql = """INSERT INTO clients (id, name, phone, email, city, region, address, create_on, updated_on) VALUES (:id, :name, :tel, :email, :city, :region, :address, :create_on, :updated_on) returning *;"""
                res = await conn.execute(text(sql), {
                    'id': idnumb, 
                    'name': name, 
                    'tel': phone, 
                    'email': email,
                    'city': city,
                    'region': region,
                    'address': address,
                    'create_on': timestamp,
                    'updated_on': timestamp,
                })
                p1 = res.fetchone()
                return p1
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
        

async def select_data():
    try:
        async with async_engine.connect() as conn:
            sql = text("SELECT * FROM clients;")
            res = await conn.execute(sql)
            p1 = res.mappings().first()
            return p1
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    

async def select_client(client_id: str):
    try:
        async with async_engine.connect() as conn:
            sql = """SELECT * FROM clients WHERE clients.id = :client_id"""
            res = await conn.execute(text(sql), {"client_id": client_id})
            p1 = res.fetchone()  # Получение первой записи как словаря
            return p1
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
