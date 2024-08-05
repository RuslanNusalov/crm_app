# from sqlalchemy import text
# from database import sync_engine
# from models.models import metadata


# # def get_123_sync():
# #     with sync_engine.connect() as coon:
# #         res = coon.execute(text("SELECT VERSION()"))
# #         print(f"{res.first()=}")

# def create_tables():
#     metadata.drop_all(sync_engine)
#     metadata.create_all(sync_engine)
