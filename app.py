"""Minimal FastAPI wrapper around Hindsight reflect(), for live demo purposes only."""

from datetime import datetime
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from hindsight_setup import get_client
from seed_data import SEED_MEETINGS

app = FastAPI(title="M&A Memory Demo")
client = get_client()

STATIC_DIR = Path(__file__).parent / "static"


class ReflectRequest(BaseModel):
    bank_id: str
    query: str


class ReflectResult(BaseModel):
    answer: str


class TimelineNote(BaseModel):
    content: str
    context: str
    timestamp: str
    week: int


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/timeline", response_model=list[TimelineNote])
def timeline() -> list[TimelineNote]:
    start_date = min(datetime.fromisoformat(note["timestamp"]) for note in SEED_MEETINGS).date()
    notes = []
    for note in SEED_MEETINGS:
        dt = datetime.fromisoformat(note["timestamp"]).date()
        week = (dt - start_date).days // 7 + 1
        notes.append(TimelineNote(**note, week=week))
    return notes


@app.post("/reflect", response_model=ReflectResult)
def reflect(request: ReflectRequest) -> ReflectResult:
    result = client.reflect(bank_id=request.bank_id, query=request.query)
    return ReflectResult(answer=result.text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
