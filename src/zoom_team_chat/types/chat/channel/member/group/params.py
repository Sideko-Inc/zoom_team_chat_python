"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostChatChannelsChannelIdMembersGroupsBodyGroupsItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    group_id: typing_extensions.Required[str]


class _SerializerPostChatChannelsChannelIdMembersGroupsBodyGroupsItem(
    pydantic.BaseModel
):
    """
    Serializer for PostChatChannelsChannelIdMembersGroupsBodyGroupsItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    group_id: str = pydantic.Field(alias="group_id")


class PostChatChannelsChannelIdMembersGroupsBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    groups: typing_extensions.NotRequired[
        typing.List[PostChatChannelsChannelIdMembersGroupsBodyGroupsItem]
    ]


class _SerializerPostChatChannelsChannelIdMembersGroupsBody(pydantic.BaseModel):
    """
    Serializer for PostChatChannelsChannelIdMembersGroupsBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    groups: typing.Optional[
        typing.List[_SerializerPostChatChannelsChannelIdMembersGroupsBodyGroupsItem]
    ] = pydantic.Field(alias="groups", default=None)