from fastapi import FastAPI


from ge_service.variables.account_variable import *

from ge_service.api_objects.account_object import *
from ge_service.database_models.account_model import *


async def create_primary_account():
    pass


async def create_platform_account():
    pass


async def get_primary_account():
    pass


async def get_platform_account():
    pass


def load_endpoints(app: FastAPI):
    pass