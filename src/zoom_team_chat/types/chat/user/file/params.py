"""File Generated by Sideko (sideko.dev)"""

from __future__ import annotations
import io
import typing
import pydantic
import typing_extensions

HttpxFile = typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]


class PostChatUsersUserIdFilesBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    file: typing_extensions.NotRequired[
        typing.Union[typing.BinaryIO, io.BufferedReader]
    ]


class _SerializerPostChatUsersUserIdFilesBody(pydantic.BaseModel):
    """
    Serializer for PostChatUsersUserIdFilesBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    @staticmethod
    def get_files_from_typed_dict(
        item: PostChatUsersUserIdFilesBody,
    ) -> typing.List[HttpxFile]:
        files: typing.List[HttpxFile] = []

        file = item.get("file", None)
        if isinstance(file, list):
            files.extend([("file", f) for f in file])
        elif file is not None:
            files.append(("file", file))

        return files


class PostChatUsersUserIdMessagesFilesBody(typing_extensions.TypedDict):
    """
    No description specified
    """

    files: typing_extensions.Required[
        typing.List[typing.Union[typing.BinaryIO, io.BufferedReader]]
    ]
    reply_main_message_id: typing_extensions.NotRequired[str]
    to_channel: typing_extensions.NotRequired[str]
    to_contact: typing_extensions.NotRequired[str]


class _SerializerPostChatUsersUserIdMessagesFilesBody(pydantic.BaseModel):
    """
    Serializer for PostChatUsersUserIdMessagesFilesBody handling case conversions
    and file omitions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    reply_main_message_id: typing.Optional[str] = pydantic.Field(
        alias="reply_main_message_id", default=None
    )
    to_channel: typing.Optional[str] = pydantic.Field(alias="to_channel", default=None)
    to_contact: typing.Optional[str] = pydantic.Field(alias="to_contact", default=None)

    @staticmethod
    def get_files_from_typed_dict(
        item: PostChatUsersUserIdMessagesFilesBody,
    ) -> typing.List[HttpxFile]:
        files: typing.List[HttpxFile] = []

        file = item.get("files", None)
        if isinstance(file, list):
            files.extend([("files", f) for f in file])
        elif file is not None:
            files.append(("files", file))

        return files