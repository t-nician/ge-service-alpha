from enum import Enum


class PlatformAccountType(str, Enum):
    DISCORD = "discord"
    MORDHAU = "mordhau"


SQLITE_DATABASE_URL = "sqlite://workspace/database.sqlite3"


TORTOISE_MODELS_PATH = "ge_service.database_models"
FOREIGN_KEY_FIELD_FOR_PRIMARY_ACCOUNT = "models.PrimaryAccount"

TABLE_NAME_PRIMARY_ACCOUNT = "primary_account"

TABLE_NAME_PLATFORM_ACCOUNT = "platform_account"
TABLE_NAME_DISCORD_ACCOUNT = "discord_account"
TABLE_NAME_MORDHAU_ACCOUNT = "mordhau_account"

RELATED_NAME_PLATFORM_ACCOUNT = "platform_account"
RELATED_NAME_DISCORD_ACCOUNT = "discord_account"
RELATED_NAME_MORDHAU_ACCOUNT = "mordhau_account"