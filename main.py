from fastapi import FastAPI
from routers import documents

app = FastAPI(title="TMSITI Backend")

app.include_router(documents.router)