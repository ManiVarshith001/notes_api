from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main import app  # import your FastAPI app from main.py

# Add CORS (optional but good for frontend use)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


handler = app
