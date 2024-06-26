"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostChatMigrationEmojiReactionsBodyReactionsItemEmojisItem(
    typing_extensions.TypedDict
):
    """
    No description specified
    """

    emoji: typing_extensions.Required[str]
    user_identifier: typing_extensions.Required[typing.List[str]]


class _SerializerPostChatMigrationEmojiReactionsBodyReactionsItemEmojisItem(
    pydantic.BaseModel
):
    """
    Serializer for PostChatMigrationEmojiReactionsBodyReactionsItemEmojisItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    emoji: str = pydantic.Field(alias="emoji")
    user_identifier: typing.List[str] = pydantic.Field(alias="user_identifier")


class PostChatMigrationMessagesBodyMessagesItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    message_timestamp: typing_extensions.Required[int]
    sender: typing_extensions.Required[str]
    to_channel: typing_extensions.NotRequired[str]
    to_contact: typing_extensions.NotRequired[typing.Union[str, str, str]]
    message: typing_extensions.NotRequired[str]
    file_ids: typing_extensions.NotRequired[typing.List[str]]
    reply_main_message_id: typing_extensions.NotRequired[str]
    reply_main_message_timestamp: typing_extensions.NotRequired[int]


class _SerializerPostChatMigrationMessagesBodyMessagesItem(pydantic.BaseModel):
    """
    Serializer for PostChatMigrationMessagesBodyMessagesItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message_timestamp: int = pydantic.Field(alias="message_timestamp")
    sender: str = pydantic.Field(alias="sender")
    to_channel: typing.Optional[str] = pydantic.Field(alias="to_channel", default=None)
    to_contact: typing.Optional[typing.Union[str, str, str]] = pydantic.Field(
        alias="to_contact", default=None
    )
    message: typing.Optional[str] = pydantic.Field(alias="message", default=None)
    file_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="file_ids", default=None
    )
    reply_main_message_id: typing.Optional[str] = pydantic.Field(
        alias="reply_main_message_id", default=None
    )
    reply_main_message_timestamp: typing.Optional[int] = pydantic.Field(
        alias="reply_main_message_timestamp", default=None
    )


class PostChatMigrationEmojiReactionsBodyReactionsItem(typing_extensions.TypedDict):
    """
    No description specified
    """

    message_id: typing_extensions.Required[str]
    message_timestamp: typing_extensions.Required[int]
    to_channel: typing_extensions.NotRequired[str]
    to_contact: typing_extensions.NotRequired[typing.Union[str, str, str]]
    emojis: typing_extensions.Required[
        typing.List[PostChatMigrationEmojiReactionsBodyReactionsItemEmojisItem]
    ]


class _SerializerPostChatMigrationEmojiReactionsBodyReactionsItem(pydantic.BaseModel):
    """
    Serializer for PostChatMigrationEmojiReactionsBodyReactionsItem handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    message_id: str = pydantic.Field(alias="message_id")
    message_timestamp: int = pydantic.Field(alias="message_timestamp")
    to_channel: typing.Optional[str] = pydantic.Field(alias="to_channel", default=None)
    to_contact: typing.Optional[typing.Union[str, str, str]] = pydantic.Field(
        alias="to_contact", default=None
    )
    emojis: typing.List[
        _SerializerPostChatMigrationEmojiReactionsBodyReactionsItemEmojisItem
    ] = pydantic.Field(alias="emojis")


class PostChatMigrationMessagesBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    messages: typing_extensions.Required[
        typing.List[PostChatMigrationMessagesBodyMessagesItem]
    ]


class _SerializerPostChatMigrationMessagesBody(pydantic.BaseModel):
    """
    Serializer for PostChatMigrationMessagesBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    messages: typing.List[_SerializerPostChatMigrationMessagesBodyMessagesItem] = (
        pydantic.Field(alias="messages")
    )


class PostChatMigrationEmojiReactionsBody(typing_extensions.TypedDict):
    """
    The person who calls the API must have the &#x60;chat_message:edit&#x60; role.
    """

    reactions: typing_extensions.Required[
        typing.List[PostChatMigrationEmojiReactionsBodyReactionsItem]
    ]


class _SerializerPostChatMigrationEmojiReactionsBody(pydantic.BaseModel):
    """
    Serializer for PostChatMigrationEmojiReactionsBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reactions: typing.List[
        _SerializerPostChatMigrationEmojiReactionsBodyReactionsItem
    ] = pydantic.Field(alias="reactions")
