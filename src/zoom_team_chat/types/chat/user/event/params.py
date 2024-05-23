"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PatchChatUsersUserIdEventsBodyParams(typing_extensions.TypedDict):
    """
    No description specified
    """

    target_id: typing_extensions.Required[str]
    target_type: typing_extensions.Required[
        typing_extensions.Literal["channel", "contact"]
    ]


class _SerializerPatchChatUsersUserIdEventsBodyParams(pydantic.BaseModel):
    """
    Serializer for PatchChatUsersUserIdEventsBodyParams handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    target_id: str = pydantic.Field(alias="target_id")
    target_type: typing_extensions.Literal["channel", "contact"] = pydantic.Field(
        alias="target_type"
    )


class PatchChatUsersUserIdEventsBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    method: typing_extensions.Required[typing_extensions.Literal["star", "unstar"]]
    params: typing_extensions.Required[PatchChatUsersUserIdEventsBodyParams]


class _SerializerPatchChatUsersUserIdEventsBody(pydantic.BaseModel):
    """
    Serializer for PatchChatUsersUserIdEventsBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    method: typing_extensions.Literal["star", "unstar"] = pydantic.Field(alias="method")
    params: _SerializerPatchChatUsersUserIdEventsBodyParams = pydantic.Field(
        alias="params"
    )