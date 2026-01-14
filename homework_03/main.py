from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping/")
async def ping():
    response = JSONResponse(
        {"message": "pong"},
        status_code=status.HTTP_200_OK,
    )
    return response

