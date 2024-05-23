"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PatchChatInvitationsBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    channel_id: typing_extensions.Required[str]
    response: typing_extensions.Required[
        typing_extensions.Literal["accept_invitation", "reject_invitation"]
    ]


class _SerializerPatchChatInvitationsBody(pydantic.BaseModel):
    """
    Serializer for PatchChatInvitationsBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    channel_id: str = pydantic.Field(alias="channel_id")
    response: typing_extensions.Literal["accept_invitation", "reject_invitation"] = (
        pydantic.Field(alias="response")
    )


class PostChatInvitationsJoinBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    invite_link: typing_extensions.Required[str]


class _SerializerPostChatInvitationsJoinBody(pydantic.BaseModel):
    """
    Serializer for PostChatInvitationsJoinBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    invite_link: str = pydantic.Field(alias="invite_link")
