import fastapi

import asyncio
import uvicorn

from ge_service.services.database_service import database_app

from ge_service.services.database_service.account_manager import *

async def get_or_create_account(
    id: int | str, type: PlatformAccountType, name: str = "name missing"
) -> PlatformAccountModel:    
    return (
            await PlatformAccountModel.get_or_none(account_id=10000)
        ) or (
            await PlatformAccountModel.create(
                primary_account=await PrimaryAccountModel.create(
                    authority_account_id=str(id),
                    authority_account_type=PlatformAccountType.DISCORD
                ),
                
                account_id=id,
                account_name=name,
                account_type=type
            )
        )


async def prelaunch():
    discord_account = await get_or_create_account(
        10000,
        PlatformAccountType.DISCORD
    )

    print(await discord_account.get_primary_account_id())


app = fastapi.FastAPI()

database_app.load_endpoints(app)
database_app.establish_database()

asyncio.run(prelaunch())
uvicorn.run(app, host="127.0.0.1", port=5000)