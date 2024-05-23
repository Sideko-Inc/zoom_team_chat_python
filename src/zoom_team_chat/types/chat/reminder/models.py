"""File Generated by Sideko (sideko.dev)"""

import io
import typing

from pydantic import (
    BaseModel as _PydanticBaseModel,
    Field as _PydanticField,
    ConfigDict as _PydanticConfigDict,
)

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class GetChatReminderResponseRemindersItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reminder_note: str = _PydanticField(alias="reminder_note")
    content: str = _PydanticField(alias="content")
    message_timestamp: int = _PydanticField(alias="message_timestamp")
    create_time: str = _PydanticField(alias="create_time")
    remind_time: str = _PydanticField(alias="remind_time")
    message_id: str = _PydanticField(alias="message_id")
    main_message_id: typing.Optional[str] = _PydanticField(
        alias="main_message_id", default=None
    )
    main_message_timestamp: typing.Optional[int] = _PydanticField(
        alias="main_message_timestamp", default=None
    )


class GetChatReminderResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    next_page_token: str = _PydanticField(alias="next_page_token")
    reminders: typing.List[GetChatReminderResponseRemindersItem] = _PydanticField(
        alias="reminders"
    )