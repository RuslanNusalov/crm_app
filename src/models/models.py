import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, \
    DateTime, UUID


metadata = MetaData()
#engine = create_engine("postgresql+psycopg2://root:pass@localhost/crm_app")

notes = Table(
    "notes",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("client_id", Integer, ForeignKey("clients.id")),
    Column("note", String),
)

clients = Table(
    "clients",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("name", String, nullable=False),
    Column("phone", String),
    Column("email", String, nullable=False),
    Column("city", String),
    Column("region", String),
    Column("address", String),
    Column("create_on", TIMESTAMP, default=datetime.UTC),
    Column("updated_on", DateTime(), default=datetime.datetime.now, onupdate=datetime.date.today),
    Column("parent_user_id", Integer),
    # Column("is_active", bool),
)
    

#metadata.create_all(engine)
