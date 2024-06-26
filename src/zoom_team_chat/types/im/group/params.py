"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PatchImGroupsGroupIdBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    name: typing_extensions.NotRequired[str]
    search_by_account: typing_extensions.NotRequired[bool]
    search_by_domain: typing_extensions.NotRequired[bool]
    search_by_ma_account: typing_extensions.NotRequired[bool]
    type: typing_extensions.NotRequired[
        typing_extensions.Literal["normal", "shared", "restricted"]
    ]


class _SerializerPatchImGroupsGroupIdBody(pydantic.BaseModel):
    """
    Serializer for PatchImGroupsGroupIdBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    search_by_account: typing.Optional[bool] = pydantic.Field(
        alias="search_by_account", default=None
    )
    search_by_domain: typing.Optional[bool] = pydantic.Field(
        alias="search_by_domain", default=None
    )
    search_by_ma_account: typing.Optional[bool] = pydantic.Field(
        alias="search_by_ma_account", default=None
    )
    type: typing.Optional[
        typing_extensions.Literal["normal", "shared", "restricted"]
    ] = pydantic.Field(alias="type", default=None)


class PostImGroupsBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    name: typing_extensions.NotRequired[str]
    search_by_account: typing_extensions.NotRequired[bool]
    search_by_domain: typing_extensions.NotRequired[bool]
    search_by_ma_account: typing_extensions.NotRequired[bool]
    type: typing_extensions.NotRequired[
        typing_extensions.Literal["normal", "shared", "restricted"]
    ]


class _SerializerPostImGroupsBody(pydantic.BaseModel):
    """
    Serializer for PostImGroupsBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    search_by_account: typing.Optional[bool] = pydantic.Field(
        alias="search_by_account", default=None
    )
    search_by_domain: typing.Optional[bool] = pydantic.Field(
        alias="search_by_domain", default=None
    )
    search_by_ma_account: typing.Optional[bool] = pydantic.Field(
        alias="search_by_ma_account", default=None
    )
    type: typing.Optional[
        typing_extensions.Literal["normal", "shared", "restricted"]
    ] = pydantic.Field(alias="type", default=None)
