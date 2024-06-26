"""File Generated by Sideko (sideko.dev)"""

import io
import typing

from pydantic import (
    BaseModel as _PydanticBaseModel,
    Field as _PydanticField,
    ConfigDict as _PydanticConfigDict,
)

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class PostChatChannelsChannelIdMembersMeResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    added_at: typing.Optional[str] = _PydanticField(alias="added_at", default=None)
    id: typing.Optional[str] = _PydanticField(alias="id", default=None)
    member_id: typing.Optional[str] = _PydanticField(alias="member_id", default=None)
