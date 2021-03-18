from typing import Optional

from tortoise.fields import CharField, ReverseRelation

from .. import models
from ..models.base import AbstractBaseModel


class Group(AbstractBaseModel):
    class Meta:
        table = "groups"

    name: str = CharField(max_length=255)
    slug: str = CharField(max_length=32, unique=True, index=True)
    channel_id: Optional[str] = CharField(max_length=32, null=True)
    channel_uri: Optional[str] = CharField(max_length=255, null=True)
    tests: ReverseRelation["models.Test"]
