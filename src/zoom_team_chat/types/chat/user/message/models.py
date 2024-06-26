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


class GetChatUsersUserIdMessagesResponseMessagesItemFilesItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    download_url: typing.Optional[str] = _PydanticField(
        alias="download_url", default=None
    )
    file_id: typing.Optional[str] = _PydanticField(alias="file_id", default=None)
    file_name: typing.Optional[str] = _PydanticField(alias="file_name", default=None)
    file_size: typing.Optional[int] = _PydanticField(alias="file_size", default=None)


class GetChatUsersUserIdMessagesResponseMessagesItemRichTextItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    start_position: typing.Optional[int] = _PydanticField(
        alias="start_position", default=None
    )
    end_position: typing.Optional[int] = _PydanticField(
        alias="end_position", default=None
    )
    format_type: typing.Optional[
        typing_extensions.Literal[
            "Bold",
            "Italic",
            "Strikethrough",
            "BulletedList",
            "NumberedList",
            "Underline",
            "FontSize",
            "FontColor",
            "BackgroundColor",
            "LeftIndent",
            "Paragraph",
            "Quote",
            "AddLink",
        ]
    ] = _PydanticField(alias="format_type", default=None)
    format_attr: typing.Optional[str] = _PydanticField(
        alias="format_attr", default=None
    )


class GetChatUsersUserIdMessagesResponseMessagesItemReactionsItemSendersItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    user_id: typing.Optional[str] = _PydanticField(alias="user_id", default=None)
    member_id: typing.Optional[str] = _PydanticField(alias="member_id", default=None)


class GetChatUsersUserIdMessagesResponseMessagesItemAtItemsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    at_contact: typing.Optional[str] = _PydanticField(alias="at_contact", default=None)
    at_contact_member_id: typing.Optional[str] = _PydanticField(
        alias="at_contact_member_id", default=None
    )
    at_type: typing.Optional[int] = _PydanticField(alias="at_type", default=None)
    end_position: typing.Optional[int] = _PydanticField(
        alias="end_position", default=None
    )
    start_position: typing.Optional[int] = _PydanticField(
        alias="start_position", default=None
    )


class GetChatUsersUserIdMessagesResponseInteractiveCardsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_id: typing.Optional[str] = _PydanticField(alias="card_id", default=None)
    card_json: typing.Optional[str] = _PydanticField(alias="card_json", default=None)


class GetChatUsersUserIdMessagesMessageIdResponseRichTextItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    start_position: typing.Optional[int] = _PydanticField(
        alias="start_position", default=None
    )
    end_position: typing.Optional[int] = _PydanticField(
        alias="end_position", default=None
    )
    format_type: typing.Optional[
        typing_extensions.Literal[
            "Bold",
            "Italic",
            "Strikethrough",
            "BulletedList",
            "NumberedList",
            "Underline",
            "FontSize",
            "FontColor",
            "BackgroundColor",
            "LeftIndent",
            "Paragraph",
            "Quote",
            "AddLink",
        ]
    ] = _PydanticField(alias="format_type", default=None)
    format_attr: typing.Optional[str] = _PydanticField(
        alias="format_attr", default=None
    )


class GetChatUsersUserIdMessagesMessageIdResponseFilesItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    download_url: typing.Optional[str] = _PydanticField(
        alias="download_url", default=None
    )
    file_id: typing.Optional[str] = _PydanticField(alias="file_id", default=None)
    file_name: typing.Optional[str] = _PydanticField(alias="file_name", default=None)
    file_size: typing.Optional[int] = _PydanticField(alias="file_size", default=None)


class GetChatUsersUserIdMessagesMessageIdResponseReactionsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    emoji: typing.Optional[str] = _PydanticField(alias="emoji", default=None)
    total_count: typing.Optional[int] = _PydanticField(
        alias="total_count", default=None
    )
    user_ids: typing.Optional[typing.List[str]] = _PydanticField(
        alias="user_ids", default=None
    )
    member_ids: typing.Optional[typing.List[str]] = _PydanticField(
        alias="member_ids", default=None
    )


class GetChatUsersUserIdMessagesMessageIdResponseAtItemsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    at_contact: typing.Optional[str] = _PydanticField(alias="at_contact", default=None)
    at_contact_member_id: typing.Optional[str] = _PydanticField(
        alias="at_contact_member_id", default=None
    )
    at_type: typing.Optional[int] = _PydanticField(alias="at_type", default=None)
    end_position: typing.Optional[int] = _PydanticField(
        alias="end_position", default=None
    )
    start_position: typing.Optional[int] = _PydanticField(
        alias="start_position", default=None
    )


class GetChatUsersUserIdMessagesMessageIdResponseInteractiveCardsItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_id: typing.Optional[str] = _PydanticField(alias="card_id", default=None)
    card_json: typing.Optional[str] = _PydanticField(alias="card_json", default=None)


class GetChatUsersUserIdMessagesMessageIdThreadResponseMessagesItemReactionsItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    emoji_id: typing.Optional[str] = _PydanticField(alias="emoji_id", default=None)
    count: typing.Optional[int] = _PydanticField(alias="count", default=None)
    is_sender: typing.Optional[bool] = _PydanticField(alias="is_sender", default=None)


class GetChatUsersUserIdMessagesMessageIdThreadResponseMessagesItemFilesItem(
    _PydanticBaseModel
):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    file_id: typing.Optional[str] = _PydanticField(alias="file_id", default=None)
    file_name: typing.Optional[str] = _PydanticField(alias="file_name", default=None)
    file_size: typing.Optional[int] = _PydanticField(alias="file_size", default=None)
    download_url: typing.Optional[str] = _PydanticField(
        alias="download_url", default=None
    )


class PostChatUsersUserIdMessagesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: typing.Optional[str] = _PydanticField(alias="id", default=None)


class GetChatUsersUserIdMessagesResponseMessagesItemReactionsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    emoji: typing.Optional[str] = _PydanticField(alias="emoji", default=None)
    total_count: typing.Optional[int] = _PydanticField(
        alias="total_count", default=None
    )
    senders: typing.Optional[
        typing.List[
            GetChatUsersUserIdMessagesResponseMessagesItemReactionsItemSendersItem
        ]
    ] = _PydanticField(alias="senders", default=None)


class GetChatUsersUserIdMessagesMessageIdResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bot_message: typing.Optional[typing.Dict[str, typing.Any]] = _PydanticField(
        alias="bot_message", default=None
    )
    date_time: typing.Optional[str] = _PydanticField(alias="date_time", default=None)
    download_url: typing.Optional[str] = _PydanticField(
        alias="download_url", default=None
    )
    file_id: typing.Optional[str] = _PydanticField(alias="file_id", default=None)
    file_name: typing.Optional[str] = _PydanticField(alias="file_name", default=None)
    file_size: typing.Optional[int] = _PydanticField(alias="file_size", default=None)
    rich_text: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesMessageIdResponseRichTextItem]
    ] = _PydanticField(alias="rich_text", default=None)
    files: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesMessageIdResponseFilesItem]
    ] = _PydanticField(alias="files", default=None)
    id: typing.Optional[str] = _PydanticField(alias="id", default=None)
    message: typing.Optional[str] = _PydanticField(alias="message", default=None)
    reactions: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesMessageIdResponseReactionsItem]
    ] = _PydanticField(alias="reactions", default=None)
    reply_main_message_id: typing.Optional[str] = _PydanticField(
        alias="reply_main_message_id", default=None
    )
    reply_main_message_timestamp: typing.Optional[int] = _PydanticField(
        alias="reply_main_message_timestamp", default=None
    )
    sender: typing.Optional[str] = _PydanticField(alias="sender", default=None)
    sender_member_id: typing.Optional[str] = _PydanticField(
        alias="sender_member_id", default=None
    )
    sender_display_name: typing.Optional[str] = _PydanticField(
        alias="sender_display_name", default=None
    )
    timestamp: typing.Optional[int] = _PydanticField(alias="timestamp", default=None)
    message_url: typing.Optional[str] = _PydanticField(
        alias="message_url", default=None
    )
    at_items: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesMessageIdResponseAtItemsItem]
    ] = _PydanticField(alias="at_items", default=None)
    interactive_cards: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesMessageIdResponseInteractiveCardsItem]
    ] = _PydanticField(alias="interactive_cards", default=None)


class GetChatUsersUserIdMessagesMessageIdThreadResponseMessagesItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    msg_id: str = _PydanticField(alias="msg_id")
    message: str = _PydanticField(alias="message")
    is_reply: bool = _PydanticField(alias="is_reply")
    timestamp: int = _PydanticField(alias="timestamp")
    reactions: typing.Optional[
        typing.List[
            GetChatUsersUserIdMessagesMessageIdThreadResponseMessagesItemReactionsItem
        ]
    ] = _PydanticField(alias="reactions", default=None)
    last_reply_time: typing.Optional[int] = _PydanticField(
        alias="last_reply_time", default=None
    )
    is_followed: typing.Optional[bool] = _PydanticField(
        alias="is_followed", default=None
    )
    files: typing.Optional[
        typing.List[
            GetChatUsersUserIdMessagesMessageIdThreadResponseMessagesItemFilesItem
        ]
    ] = _PydanticField(alias="files", default=None)


class GetChatUsersUserIdMessagesResponseMessagesItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bot_message: typing.Optional[typing.Dict[str, typing.Any]] = _PydanticField(
        alias="bot_message", default=None
    )
    date_time: typing.Optional[str] = _PydanticField(alias="date_time", default=None)
    files: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesResponseMessagesItemFilesItem]
    ] = _PydanticField(alias="files", default=None)
    rich_text: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesResponseMessagesItemRichTextItem]
    ] = _PydanticField(alias="rich_text", default=None)
    download_url: typing.Optional[str] = _PydanticField(
        alias="download_url", default=None
    )
    file_id: typing.Optional[str] = _PydanticField(alias="file_id", default=None)
    file_name: typing.Optional[str] = _PydanticField(alias="file_name", default=None)
    file_size: typing.Optional[int] = _PydanticField(alias="file_size", default=None)
    id: typing.Optional[str] = _PydanticField(alias="id", default=None)
    message: typing.Optional[str] = _PydanticField(alias="message", default=None)
    reactions: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesResponseMessagesItemReactionsItem]
    ] = _PydanticField(alias="reactions", default=None)
    reply_main_message_id: typing.Optional[str] = _PydanticField(
        alias="reply_main_message_id", default=None
    )
    reply_main_message_timestamp: typing.Optional[int] = _PydanticField(
        alias="reply_main_message_timestamp", default=None
    )
    sender: typing.Optional[str] = _PydanticField(alias="sender", default=None)
    sender_member_id: typing.Optional[str] = _PydanticField(
        alias="sender_member_id", default=None
    )
    sender_display_name: typing.Optional[str] = _PydanticField(
        alias="sender_display_name", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal["Deleted", "Edited", "Normal"]
    ] = _PydanticField(alias="status", default=None)
    timestamp: typing.Optional[int] = _PydanticField(alias="timestamp", default=None)
    at_items: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesResponseMessagesItemAtItemsItem]
    ] = _PydanticField(alias="at_items", default=None)


class GetChatUsersUserIdMessagesMessageIdThreadResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    total: int = _PydanticField(alias="total")
    messages: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesMessageIdThreadResponseMessagesItem]
    ] = _PydanticField(alias="messages", default=None)


class GetChatUsersUserIdMessagesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    date: typing.Optional[str] = _PydanticField(alias="date", default=None)
    from_field: typing.Optional[str] = _PydanticField(alias="from", default=None)
    messages: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesResponseMessagesItem]
    ] = _PydanticField(alias="messages", default=None)
    next_page_token: typing.Optional[str] = _PydanticField(
        alias="next_page_token", default=None
    )
    page_size: typing.Optional[int] = _PydanticField(alias="page_size", default=None)
    to: typing.Optional[str] = _PydanticField(alias="to", default=None)
    interactive_cards: typing.Optional[
        typing.List[GetChatUsersUserIdMessagesResponseInteractiveCardsItem]
    ] = _PydanticField(alias="interactive_cards", default=None)
