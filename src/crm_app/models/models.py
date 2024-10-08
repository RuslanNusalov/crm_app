from sqlalchemy import MetaData, Table, Column, String, ForeignKey, \
UUID
from sqlalchemy.dialects.postgresql import TIMESTAMP

metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("note", String),
    Column("client_id", UUID, ForeignKey("clients.id", ondelete='CASCADE')),

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
    Column("create_on", TIMESTAMP(timezone=True)),
    Column("updated_on", TIMESTAMP(timezone=True)),
    # Column("is_active", bool),
)
