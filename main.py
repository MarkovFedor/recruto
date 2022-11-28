from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def helloMessage(name: str ="", message: str = ""):
    return f"Hello {name}! {message}!"
