import uvicorn

from config import port, hostname


if __name__ == "__main__":
    uvicorn.run(app="config:app", port=port, reload=True, host=hostname)
