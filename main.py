from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from journaling import generate_reflection
from meditation import create_meditation_script

app = FastAPI()
journal_log = []
# In-memory storage (temporary, resets when server restarts)
mood_data = []

class MoodEntry(BaseModel):
    day: str
    mood: int

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "SoulSync backend is running!"}

@app.post("/journal/")
def journal(entry: str = Form(...)):
    try:
        reflection = generate_reflection(entry)
        journal_log.append({"entry": entry, "reflection": reflection})
        return {"reflection": reflection}
    except Exception as e:
        print("Error:", e)
        return {"reflection": "⚠️ Something went wrong. Please try again later."}

@app.get("/journal/log/")
def get_journal_log():
    return journal_log 

@app.delete("/journal/log/clear")
def clear_journal_log():
    journal_log.clear()
    return {"message": "✅ Journal log cleared!"}

@app.post("/meditate/")
def meditate(mood: str = Form(...)):
    return {"meditation": create_meditation_script(mood)}

# ✅ NEW: Save mood entry
@app.post("/mood/")
def save_mood(entry: MoodEntry):
    mood_data.append(entry)
    return {"message": "Mood saved successfully!"}

# ✅ NEW: Get mood history
@app.get("/mood/")
def get_mood_history():
    return mood_data
