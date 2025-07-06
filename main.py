from fastapi import FastAPI
from routers import users, menu, documents

app = FastAPI(title="TMSITI Full Backend")

app.include_router(users.router)
app.include_router(menu.router)
app.include_router(documents.router)
