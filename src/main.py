import fastapi

import asyncio
import uvicorn

from ge_service.services.database_service import database_app
from ge_service.services.database_service import account_manager

async def prelaunch():    
    discord_account = await account_manager.DiscordAccountModel.get(
        account_id="1000"
    )
    
    discord_pydantic = await account_manager.discord_account_model_to_pydantic(
        discord_account
    )
    
    print(discord_pydantic)


app = fastapi.FastAPI()

database_app.load_endpoints(app)
database_app.establish_database()

asyncio.run(prelaunch())
uvicorn.run(app, host="127.0.0.1", port=5000)