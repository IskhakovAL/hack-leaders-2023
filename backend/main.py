from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.views import node, users


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(node)
app.include_router(users)
