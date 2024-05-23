"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostChatMigrationUsersIdentifierChannelsBodyMembersItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    identifier: typing_extensions.Required[str]
    role: typing_extensions.NotRequired[typing_extensions.Literal["admin", "member"]]


class _SerializerPostChatMigrationUsersIdentifierChannelsBodyMembersItem(
    pydantic.BaseModel
):
    """
    Serializer for PostChatMigrationUsersIdentifierChannelsBodyMembersItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    identifier: str = pydantic.Field(alias="identifier")
    role: typing.Optional[typing_extensions.Literal["admin", "member"]] = (
        pydantic.Field(alias="role", default=None)
    )


class PostChatMigrationUsersIdentifierChannelsBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    members: typing_extensions.Required[
        typing.List[PostChatMigrationUsersIdentifierChannelsBodyMembersItem]
    ]
    type: typing_extensions.Required[int]
    name: typing_extensions.Required[str]
    created_time: typing_extensions.Required[str]


class _SerializerPostChatMigrationUsersIdentifierChannelsBody(pydantic.BaseModel):
    """
    Serializer for PostChatMigrationUsersIdentifierChannelsBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    members: typing.List[
        _SerializerPostChatMigrationUsersIdentifierChannelsBodyMembersItem
    ] = pydantic.Field(alias="members")
    type: int = pydantic.Field(alias="type")
    name: str = pydantic.Field(alias="name")
    created_time: str = pydantic.Field(alias="created_time")