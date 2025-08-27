from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


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



@app.get("/")
def root():
    return RedirectResponse(url="/docs")




