from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestData(BaseModel):
    language: str
    text: str

@app.post("/chain/")
async def chain(data: RequestData):
    return {"message": f"Translated {data.text} to {data.language}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
