from datetime import datetime

from bson import ObjectId
from bson.errors import InvalidId
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


# class ObjectIdField(str):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate
#
#     @classmethod
#     def validate(cls, value):
#         try:
#             return ObjectId(str(value))
#         except InvalidId:
#             raise ValueError("Not a valid ObjectId")


class Document(BaseModel):
    value: int
    dt: datetime

    # class Config:
    #     populate_by_name = True
    #     arbitrary_types_allowed = True
    #     json_encoders = {ObjectId: str}


class AvgResponse(BaseModel):
    dataset: list[int]
    labels: list[datetime]
