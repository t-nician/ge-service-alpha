from typing import Awaitable, Callable

from tortoise.models import Model
from tortoise.fields import (
    TextField, BigIntField, 
    ForeignKeyField, CharEnumField, ReverseRelation
)

from tortoise.contrib.pydantic import pydantic_model_creator

from ge_service.variables.account_variable import *


class PrimaryAccountModel(Model):
    authority_account_id = TextField()
    authority_account_type = CharEnumField(PlatformAccountType)
    
    class Meta:
        table = TABLE_NAME_PRIMARY_ACCOUNT


class PlatformAccountModel(Model):
    primary_account = ForeignKeyField(
        FOREIGN_KEY_FIELD_FOR_PRIMARY_ACCOUNT,
        related_name=RELATED_NAME_PLATFORM_ACCOUNT
    )
    
    account_id = TextField(primary_key=True)
    account_name = TextField()
    
    account_type = CharEnumField(PlatformAccountType)
    
    async def get_primary_account_id(self) -> int:
        await self.fetch_related(TABLE_NAME_PRIMARY_ACCOUNT)
        return self.primary_account.id
    
    class Meta:
        table = TABLE_NAME_PLATFORM_ACCOUNT


class DiscordAccountModel(PlatformAccountModel):
    primary_account = ForeignKeyField(
        FOREIGN_KEY_FIELD_FOR_PRIMARY_ACCOUNT,
        related_name=RELATED_NAME_DISCORD_ACCOUNT
    )
    
    account_type = None
    
    class Meta:
        table = TABLE_NAME_DISCORD_ACCOUNT
        
    
class MordhauAccountModel(PlatformAccountModel):
    primary_account = ForeignKeyField(
        FOREIGN_KEY_FIELD_FOR_PRIMARY_ACCOUNT,
        related_name=RELATED_NAME_MORDHAU_ACCOUNT
    )
    
    account_type = None
    
    class Meta:
        table = TABLE_NAME_MORDHAU_ACCOUNT