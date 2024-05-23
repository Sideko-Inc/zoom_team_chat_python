"""File Generated by Sideko (sideko.dev)"""

import io
import typing
import typing_extensions
from pydantic import (
    BaseModel as _PydanticBaseModel,
    Field as _PydanticField,
    ConfigDict as _PydanticConfigDict,
)

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class GetChatSpacesResponseSharedSpacesItemSpaceOwner(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    user_id: typing.Optional[str] = _PydanticField(alias="user_id", default=None)
    member_id: str = _PydanticField(alias="member_id")
    email: typing.Optional[str] = _PydanticField(alias="email", default=None)
    display_name: str = _PydanticField(alias="display_name")
    is_external_user: bool = _PydanticField(alias="is_external_user")


class GetChatSpacesSpaceIdResponseOwner(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    user_id: typing.Optional[str] = _PydanticField(alias="user_id", default=None)
    member_id: str = _PydanticField(alias="member_id")
    email: typing.Optional[str] = _PydanticField(alias="email", default=None)
    display_name: str = _PydanticField(alias="display_name ")
    is_external_user: bool = _PydanticField(alias="is_external_user")


class GetChatSpacesSpaceIdResponseSpaceSettings(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allow_to_add_external_users: typing.Optional[int] = _PydanticField(
        alias="allow_to_add_external_users", default=None
    )
    add_member_permissions: typing.Optional[int] = _PydanticField(
        alias="add_member_permissions", default=None
    )
    create_channels_permission: typing.Optional[int] = _PydanticField(
        alias="create_channels_permission", default=None
    )


class PostChatSpacesResponseSpaceMembersItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    identifier: typing.Optional[str] = _PydanticField(alias="identifier", default=None)
    role: typing.Optional[typing_extensions.Literal["admin", "member", "owner"]] = (
        _PydanticField(alias="role", default=None)
    )


class PostChatSpacesResponseSpaceSettings(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allow_to_add_external_users: typing.Optional[int] = _PydanticField(
        alias="allow_to_add_external_users", default=None
    )
    add_member_permissions: typing.Optional[int] = _PydanticField(
        alias="add_member_permissions", default=None
    )
    create_channels_permission: typing.Optional[int] = _PydanticField(
        alias="create_channels_permission", default=None
    )


class GetChatSpacesResponseSharedSpacesItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    space_id: str = _PydanticField(alias="space_id")
    space_name: str = _PydanticField(alias="space_name")
    space_desc: typing.Optional[str] = _PydanticField(alias="space_desc", default=None)
    space_owner: GetChatSpacesResponseSharedSpacesItemSpaceOwner = _PydanticField(
        alias="space_owner"
    )


class GetChatSpacesSpaceIdResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    space_id: str = _PydanticField(alias="space_id")
    space_name: str = _PydanticField(alias="space_name")
    space_desc: typing.Optional[str] = _PydanticField(alias="space_desc", default=None)
    owner: GetChatSpacesSpaceIdResponseOwner = _PydanticField(alias="owner")
    space_settings: GetChatSpacesSpaceIdResponseSpaceSettings = _PydanticField(
        alias="space_settings"
    )


class PostChatSpacesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    space_id: str = _PydanticField(alias="space_id")
    channel_id: str = _PydanticField(alias="channel_id")
    space_name: str = _PydanticField(alias="space_name")
    space_desc: typing.Optional[str] = _PydanticField(alias="space_desc", default=None)
    space_members: typing.Optional[
        typing.List[PostChatSpacesResponseSpaceMembersItem]
    ] = _PydanticField(alias="space_members", default=None)
    space_settings: typing.Optional[PostChatSpacesResponseSpaceSettings] = (
        _PydanticField(alias="space_settings", default=None)
    )


class GetChatSpacesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    next_page_token: typing.Optional[str] = _PydanticField(
        alias="next_page_token", default=None
    )
    page_size: typing.Optional[int] = _PydanticField(alias="page_size", default=None)
    shared_spaces: typing.List[GetChatSpacesResponseSharedSpacesItem] = _PydanticField(
        alias="shared_spaces"
    )
