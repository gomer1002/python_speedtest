from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi import Request
import time

app = FastAPI()


@app.get("/")
async def root():
    return FileResponse("index.html", status_code=200)


@app.get("/generate-data")
async def generate_data(size_in_mb: int = 10):
    data = "0" * (size_in_mb * 1024 * 1024)
    return JSONResponse(content=data, media_type="application/octet-stream")


@app.post("/upload-data")
async def upload_data(request: Request):
    start_time = time.time()
    await request.body()
    elapsed_time = time.time() - start_time
    return {"upload_time": elapsed_time}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
