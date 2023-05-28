from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.views import node, users, platforms


app = FastAPI(docs_url='/api/docs',
              redoc_url='/api/redoc',
              openapi_url='/api/openapi.json')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(node)
app.include_router(users)
app.include_router(platforms)
