from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class GroupType(Enum):
    hour = "hour"
    day = "day"
    month = "month"


class RequestData(BaseModel):
    dt_from: datetime
    dt_upto: datetime
    group_type: GroupType


class Document(BaseModel):
    value: int
    dt: datetime


class AvgResponse(BaseModel):
    dataset: list[int]
    labels: list[str]
