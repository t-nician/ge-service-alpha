import asyncio

from fastapi import FastAPI
from tortoise import Tortoise

from ge_service.services.database_service import (
    account_manager, moderation_manager
)

from ge_service.variables.account_variable import *


async def __initialize_tortoise():
    await Tortoise.init(
        db_url=SQLITE_DATABASE_URL,
        modules={
            "models": [
                TORTOISE_MODELS_PATH
            ]
        }
    )
    
    await Tortoise.generate_schemas()


def load_endpoints(app: FastAPI):
    account_manager.load_endpoints(app)
    moderation_manager.load_endpoints(app)


def establish_database():
    asyncio.run(__initialize_tortoise())