# FastAPI - Test CRM for real estate

A small CRM system for real estate is made for a real business task. 
There are pytest tests.
The project uses CRUD with Pydantic, SqlAlchemy and Alembic.
API documentation is available in Swagger

Endpoint map with documentation for 127.0.0.1 (standard host + port):
- Swagger <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs


# Launch project on Ubuntu with python3.10.4 and PostgreSQL 15.4:
1. `git clone <project_url>`
2. `cd <project_name>`
3. `pyenv local 3.12.4`
4. `poetry install`
5. `poetry update`
6. `cd src/crm_app`
7. `alembic upgrade head`
8. `uvicorn main:app --reload`
