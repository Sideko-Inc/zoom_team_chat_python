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


class DeleteChatSpacesSpaceIdAdminsResponseUsersItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    user_id: str = _PydanticField(alias="user_id")
    member_id: str = _PydanticField(alias="member_id")
    is_external_user: bool = _PydanticField(alias="is_external_user")
    operation_status: typing_extensions.Literal["successful", "unsuccessful"] = (
        _PydanticField(alias="operation_status")
    )


class PostChatSpacesSpaceIdAdminsResponseUsersItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    user_id: str = _PydanticField(alias="user_id")
    member_id: str = _PydanticField(alias="member_id")
    is_external_user: bool = _PydanticField(alias="is_external_user")
    operation_status: typing_extensions.Literal["successful", "unsuccessful"] = (
        _PydanticField(alias="operation_status")
    )


class DeleteChatSpacesSpaceIdAdminsResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    successful_operations_count: int = _PydanticField(
        alias="successful_operations_count"
    )
    unsuccessful_operations_count: int = _PydanticField(
        alias="unsuccessful_operations_count"
    )
    users: typing.List[DeleteChatSpacesSpaceIdAdminsResponseUsersItem] = _PydanticField(
        alias="users"
    )


class PostChatSpacesSpaceIdAdminsResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    successful_operations_count: int = _PydanticField(
        alias="successful_operations_count"
    )
    unsuccessful_operations_count: int = _PydanticField(
        alias="unsuccessful_operations_count"
    )
    users: typing.List[PostChatSpacesSpaceIdAdminsResponseUsersItem] = _PydanticField(
        alias="users"
    )
