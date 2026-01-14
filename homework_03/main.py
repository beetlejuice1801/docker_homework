import uvicorn
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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)