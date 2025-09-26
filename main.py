import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def read_root():
    return {"message": "Hello, FastAPI!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        use_colors=True,
    )