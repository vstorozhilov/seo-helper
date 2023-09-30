from fastapi import FastAPI
from .check_url import check_url

app = FastAPI()
app.include_router(check_url.router)

@app.get("/")
async def root():
    return {"message": "Hello from SEOHelper!"}
