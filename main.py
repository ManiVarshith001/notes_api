from fastapi import FastAPI, HTTPException

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your local React dev server + your future Vercel URL
origins = [
    "http://localhost:5173",            # Vite dev server
    "https://your-frontend.vercel.app", # replace later after deploy
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Fake in-memory DB
notes = {}

@app.post("/notes/")
def create_note(note_id: int, content: str):
    if note_id in notes:
        raise HTTPException(status_code=400, detail="Note lready exists")
    notes[note_id] = content
    return {"message": "Note created", "note": {note_id: content}}

@app.get("/notes/{note_id}")
def read_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"note": {note_id: notes[note_id]}}

@app.put("/notes/{note_id}")
def update_note(note_id: int, content: str):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    notes[note_id] = content
    return {"message": "Note updated", "note": {note_id: content}}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes[note_id]
    return {"message": "Note deleted"}

