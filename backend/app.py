from fastapi import APIRouter, FastAPI
import uvicorn
from api import router
from version import __version__

app = FastAPI(title="Wetest api", version=__version__)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app="app:app", host="127.0.0.1", port=8888, reload=True)
