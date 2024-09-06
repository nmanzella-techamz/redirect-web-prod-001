from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from backend import link_click_redirection, home

load_dotenv()

app = FastAPI()

@app.get("/org/{org}")
async def link_click_redirection_router(org: str):
    return await link_click_redirection(org)

@app.get("/", response_class=HTMLResponse)
async def home_router():
    return await home()