from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, \
    create_engine, DateTime


metadata = MetaData()
engine = create_engine("postgresql+psycopg2://root:pass@localhost/crm_app")

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("client_id", Integer, ForeignKey("clients.id")),
    Column("note", String),
)

clients = Table(
    "clients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("phone", String)
    Column("email", String, nullable=False),
    Column("city", String),
    Column("region", String),
    Column("address", String),
    Column("create_on", TIMESTAMP, default=datetime.utcnow),
    Column("updated_on", DateTime(), default=datetime.now, onupdate=datetime.now),
    Column("parent_user_id", Integer),
    Column("is_active", bool)
)


metadata.create_all(engine)
