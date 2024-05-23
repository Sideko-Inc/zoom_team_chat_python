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


class GetChatChannelsChannelIdMembersGroupsResponseGroupsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    group_id: str = _PydanticField(alias="group_id")
    group_name: str = _PydanticField(alias="group_name")


class PostChatChannelsChannelIdMembersGroupsResponseGroupsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    group_id: str = _PydanticField(alias="group_id")
    group_name: str = _PydanticField(alias="group_name")


class GetChatChannelsChannelIdMembersGroupsResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    groups: typing.List[GetChatChannelsChannelIdMembersGroupsResponseGroupsItem] = (
        _PydanticField(alias="groups")
    )
    channel_id: str = _PydanticField(alias="channel_id")


class PostChatChannelsChannelIdMembersGroupsResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    added_at: str = _PydanticField(alias="added_at")
    groups: typing.List[PostChatChannelsChannelIdMembersGroupsResponseGroupsItem] = (
        _PydanticField(alias="groups")
    )
