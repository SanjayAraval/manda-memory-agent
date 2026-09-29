"""Minimal FastAPI wrapper around Hindsight reflect(), for live demo purposes only."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from hindsight_setup import get_client

app = FastAPI(title="M&A Memory Demo")
client = get_client()

STATIC_DIR = Path(__file__).parent / "static"


class ReflectRequest(BaseModel):
    bank_id: str
    query: str


class ReflectResult(BaseModel):
    answer: str


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/reflect", response_model=ReflectResult)
def reflect(request: ReflectRequest) -> ReflectResult:
    result = client.reflect(bank_id=request.bank_id, query=request.query)
    return ReflectResult(answer=result.text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
