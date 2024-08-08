from tortoise.models import Model
from tortoise.fields import (
    TextField, BigIntField, 
    ForeignKeyField, CharEnumField
)


from ge_service.variables.account_variable import *


class PrimaryAccount(Model):
    authority_account_id = TextField()
    authority_account_type = CharEnumField(PlatformAccountType)
    
    class Meta:
        table = TABLE_NAME_PRIMARY_ACCOUNT


class PlatformAccount(Model):
    primary_account = ForeignKeyField(
        FOREIGN_KEY_FIELD_FOR_PRIMARY_ACCOUNT,
        related_name=RELATED_NAME_PLATFORM_ACCOUNT
    )
    
    account_id = TextField(primary_key=True)
    account_name = TextField()
    
    account_type = CharEnumField(PlatformAccountType)
    
    class Meta:
        table = TABLE_NAME_PLATFORM_ACCOUNT


class DiscordAccount(PlatformAccount):
    primary_account = ForeignKeyField(
        FOREIGN_KEY_FIELD_FOR_PRIMARY_ACCOUNT,
        related_name=RELATED_NAME_DISCORD_ACCOUNT
    )
    
    account_type = None
    
    class Meta:
        table = TABLE_NAME_DISCORD_ACCOUNT
        

class MordhauAccount(PlatformAccount):
    primary_account = ForeignKeyField(
        FOREIGN_KEY_FIELD_FOR_PRIMARY_ACCOUNT,
        related_name=RELATED_NAME_MORDHAU_ACCOUNT
    )
    
    account_type = None
    
    class Meta:
        table = TABLE_NAME_MORDHAU_ACCOUNT
        