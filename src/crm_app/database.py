from sqlalchemy.ext.asyncio import create_async_engine
from crm_app.config import settings


async_engine = create_async_engine(
    url=settings.DATABASE_URL_ASYNCPG,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


# with sync_engine.connect() as conn:
#     res = conn.execute(text("SELECT VERSION()"))
#     print(f"{res.first()=}")