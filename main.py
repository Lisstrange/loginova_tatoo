import fastapi
import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="loginova tatoo"
)
app.mount("/assets", StaticFiles(directory="templates/MyPortfolio/assets"), name="assets")
templates = Jinja2Templates(directory="templates/MyPortfolio")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/login")
# async def home(request: Request):
#     return templates.TemplateResponse("login.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True
    )
