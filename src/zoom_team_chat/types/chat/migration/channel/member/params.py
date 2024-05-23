"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostChatMigrationChannelsChannelIdMembersBodyMembersItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    identifier: typing_extensions.Required[str]
    role: typing_extensions.NotRequired[typing_extensions.Literal["member", "admin"]]


class _SerializerPostChatMigrationChannelsChannelIdMembersBodyMembersItem(
    pydantic.BaseModel
):
    """
    Serializer for PostChatMigrationChannelsChannelIdMembersBodyMembersItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    identifier: str = pydantic.Field(alias="identifier")
    role: typing.Optional[typing_extensions.Literal["member", "admin"]] = (
        pydantic.Field(alias="role", default=None)
    )


class PostChatMigrationChannelsChannelIdMembersBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    members: typing_extensions.Required[
        typing.List[PostChatMigrationChannelsChannelIdMembersBodyMembersItem]
    ]


class _SerializerPostChatMigrationChannelsChannelIdMembersBody(pydantic.BaseModel):
    """
    Serializer for PostChatMigrationChannelsChannelIdMembersBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    members: typing.List[
        _SerializerPostChatMigrationChannelsChannelIdMembersBodyMembersItem
    ] = pydantic.Field(alias="members")
