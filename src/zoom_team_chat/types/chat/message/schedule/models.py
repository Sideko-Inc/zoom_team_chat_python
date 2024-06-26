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


class GetChatMessagesScheduleResponseMessagesItemRichTextItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    start_position: int = _PydanticField(alias="start_position")
    end_position: int = _PydanticField(alias="end_position")
    format_type: typing_extensions.Literal[
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
    ] = _PydanticField(alias="format_type")
    format_attr: str = _PydanticField(alias="format_attr")


class GetChatMessagesScheduleResponseMessagesItemFilesItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    download_url: str = _PydanticField(alias="download_url")
    file_id: str = _PydanticField(alias="file_id")
    file_name: str = _PydanticField(alias="file_name")
    file_size: int = _PydanticField(alias="file_size")


class GetChatMessagesScheduleResponseMessagesItemAtItemsItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    at_contact: str = _PydanticField(alias="at_contact")
    at_contact_member_id: str = _PydanticField(alias="at_contact_member_id")
    at_type: int = _PydanticField(alias="at_type")
    end_position: int = _PydanticField(alias="end_position")
    start_position: int = _PydanticField(alias="start_position")


class GetChatMessagesScheduleResponseMessagesItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    draft_id: str = _PydanticField(alias="draft_id")
    create_date: str = _PydanticField(alias="create_date")
    scheduled_time: str = _PydanticField(alias="scheduled_time")
    download_url: typing.Optional[str] = _PydanticField(
        alias="download_url", default=None
    )
    file_id: typing.Optional[str] = _PydanticField(alias="file_id", default=None)
    file_name: typing.Optional[str] = _PydanticField(alias="file_name", default=None)
    file_size: typing.Optional[int] = _PydanticField(alias="file_size", default=None)
    rich_text: typing.Optional[
        typing.List[GetChatMessagesScheduleResponseMessagesItemRichTextItem]
    ] = _PydanticField(alias="rich_text", default=None)
    files: typing.Optional[
        typing.List[GetChatMessagesScheduleResponseMessagesItemFilesItem]
    ] = _PydanticField(alias="files", default=None)
    message: str = _PydanticField(alias="message")
    reply_main_message_id: typing.Optional[str] = _PydanticField(
        alias="reply_main_message_id", default=None
    )
    reply_main_message_timestamp: typing.Optional[float] = _PydanticField(
        alias="reply_main_message_timestamp", default=None
    )
    at_items: typing.Optional[
        typing.List[GetChatMessagesScheduleResponseMessagesItemAtItemsItem]
    ] = _PydanticField(alias="at_items", default=None)


class GetChatMessagesScheduleResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    to_channel: typing.Optional[str] = _PydanticField(alias="to_channel", default=None)
    to_contact: typing.Optional[str] = _PydanticField(alias="to_contact", default=None)
    page_size: int = _PydanticField(alias="page_size")
    next_page_token: typing.Optional[str] = _PydanticField(
        alias="next_page_token", default=None
    )
    messages: typing.List[GetChatMessagesScheduleResponseMessagesItem] = _PydanticField(
        alias="messages"
    )
