"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PatchChatSpacesSpaceIdBodySpaceSettings(typing_extensions.TypedDict):
    """
    The settings of the shared space.
    """

    allow_to_add_external_users: typing_extensions.NotRequired[int]
    add_member_permissions: typing_extensions.NotRequired[int]
    create_channels_permission: typing_extensions.NotRequired[int]


class _SerializerPatchChatSpacesSpaceIdBodySpaceSettings(pydantic.BaseModel):
    """
    Serializer for PatchChatSpacesSpaceIdBodySpaceSettings handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allow_to_add_external_users: typing.Optional[int] = pydantic.Field(
        alias="allow_to_add_external_users", default=None
    )
    add_member_permissions: typing.Optional[int] = pydantic.Field(
        alias="add_member_permissions", default=None
    )
    create_channels_permission: typing.Optional[int] = pydantic.Field(
        alias="create_channels_permission", default=None
    )


class PostChatSpacesBodySpaceMembersItem(typing_extensions.TypedDict):
    """
    The shared space member.
    """

    identifier: typing_extensions.Required[str]
    role: typing_extensions.NotRequired[
        typing_extensions.Literal["admin", "member", "owner"]
    ]


class _SerializerPostChatSpacesBodySpaceMembersItem(pydantic.BaseModel):
    """
    Serializer for PostChatSpacesBodySpaceMembersItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    identifier: str = pydantic.Field(alias="identifier")
    role: typing.Optional[typing_extensions.Literal["admin", "member", "owner"]] = (
        pydantic.Field(alias="role", default=None)
    )


class PostChatSpacesBodySpaceSettings(typing_extensions.TypedDict):
    """
    The settings of the shared space.
    """

    allow_to_add_external_users: typing_extensions.NotRequired[int]
    add_member_permissions: typing_extensions.NotRequired[int]
    create_channels_permission: typing_extensions.NotRequired[int]


class _SerializerPostChatSpacesBodySpaceSettings(pydantic.BaseModel):
    """
    Serializer for PostChatSpacesBodySpaceSettings handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allow_to_add_external_users: typing.Optional[int] = pydantic.Field(
        alias="allow_to_add_external_users", default=None
    )
    add_member_permissions: typing.Optional[int] = pydantic.Field(
        alias="add_member_permissions", default=None
    )
    create_channels_permission: typing.Optional[int] = pydantic.Field(
        alias="create_channels_permission", default=None
    )


class PatchChatSpacesSpaceIdBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    space_name: typing_extensions.NotRequired[str]
    space_desc: typing_extensions.NotRequired[str]
    space_settings: typing_extensions.NotRequired[
        PatchChatSpacesSpaceIdBodySpaceSettings
    ]


class _SerializerPatchChatSpacesSpaceIdBody(pydantic.BaseModel):
    """
    Serializer for PatchChatSpacesSpaceIdBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    space_name: typing.Optional[str] = pydantic.Field(alias="space_name", default=None)
    space_desc: typing.Optional[str] = pydantic.Field(alias="space_desc", default=None)
    space_settings: typing.Optional[
        _SerializerPatchChatSpacesSpaceIdBodySpaceSettings
    ] = pydantic.Field(alias="space_settings", default=None)


class PostChatSpacesBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    space_name: typing_extensions.Required[str]
    space_desc: typing_extensions.NotRequired[str]
    space_members: typing_extensions.NotRequired[
        typing.List[PostChatSpacesBodySpaceMembersItem]
    ]
    space_settings: typing_extensions.NotRequired[PostChatSpacesBodySpaceSettings]


class _SerializerPostChatSpacesBody(pydantic.BaseModel):
    """
    Serializer for PostChatSpacesBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    space_name: str = pydantic.Field(alias="space_name")
    space_desc: typing.Optional[str] = pydantic.Field(alias="space_desc", default=None)
    space_members: typing.Optional[
        typing.List[_SerializerPostChatSpacesBodySpaceMembersItem]
    ] = pydantic.Field(alias="space_members", default=None)
    space_settings: typing.Optional[_SerializerPostChatSpacesBodySpaceSettings] = (
        pydantic.Field(alias="space_settings", default=None)
    )
