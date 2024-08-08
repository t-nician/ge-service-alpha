import fastapi

import asyncio
import uvicorn

from ge_service.services.database_service import database_app
from ge_service.services.database_service import account_manager


async def prelaunch():
    pass


app = fastapi.FastAPI()

database_app.load_endpoints(app)
database_app.establish_database()

asyncio.run(prelaunch())
uvicorn.run(app, host="127.0.0.1", port=5000)