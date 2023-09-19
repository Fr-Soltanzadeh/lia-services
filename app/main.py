import uvicorn

from config import CONFIG


if __name__ == "__main__":
    uvicorn.run(app="app:app", port=CONFIG.port, reload=True, host=CONFIG.hostname)
