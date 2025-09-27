from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "Title page", "username": "Kirill"}
    )


PROBLEM_LIST = [
    {"slug": "two-sum", "title": "Two Sum", "id": "0001", "difficulty": "00"},
    {"slug": "reverse-string", "title": "Reverse String", "id": "0002", "difficulty": "05"},
]

@app.get("/problems", response_class=HTMLResponse)
async def show_problems(request: Request):
    return templates.TemplateResponse(
        "problems.html",
        {"request": request, "problems": PROBLEM_LIST}
    )