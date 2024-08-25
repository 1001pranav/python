from fastapi import FastAPI

# TO run fastAPI 
import uvicorn

#Adding CORS middleware.
from fastapi.middleware.cors import CORSMiddleware

from router.todo import todoRouter

# List of origins that should be allowed to make requests
origins = [
    "http://localhost:3000",
    "*",  # Allow all origins
]

app = FastAPI()

# Enabling middleware for handling CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins or use ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get('/')
def read_root():
    return {'Hello': 'World'}

app.include_router(todoRouter, prefix="/todo", tags=['todo'])

if __name__ == '__main__':
    uvicorn.run("server:app", host='0.0.0.0', port=8000, reload=True)
