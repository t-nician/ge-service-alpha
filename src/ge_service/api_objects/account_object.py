from typing import Awaitable, Callable

from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator

from ge_service.database_models.account_model import *


class PrimaryAccountObject(BaseModel):
    pass


class DiscordAccountObject(BaseModel):
    pass


class MordhauAccountObject(BaseModel):
    pass


primary_account_model_to_pydantic: Callable[
    [PrimaryAccountModel], 
    Awaitable[PrimaryAccountObject]
] = pydantic_model_creator(PrimaryAccountModel).from_tortoise_orm


discord_account_model_to_pydantic: Callable[
    [DiscordAccountModel], 
    Awaitable[DiscordAccountObject]
] = pydantic_model_creator(DiscordAccountModel).from_tortoise_orm


mordhau_account_model_to_pydantic: Callable[
    [MordhauAccountModel], 
    Awaitable[MordhauAccountObject]
] = pydantic_model_creator(MordhauAccountModel).from_tortoise_orm
