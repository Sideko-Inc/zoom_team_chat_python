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


class GetChatLegalholdMattersMatterIdFilesResponseDataItem(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    file_key: str = _PydanticField(alias="file_key")
    file_count: int = _PydanticField(alias="file_count")
    file_start_date: str = _PydanticField(alias="file_start_date")
    file_end_date: str = _PydanticField(alias="file_end_date")
    ready_for_download: bool = _PydanticField(alias="ready_for_download")
    total_file_size: int = _PydanticField(alias="total_file_size")


class GetChatLegalholdMattersMatterIdFilesResponse(_PydanticBaseModel):
    model_config = _PydanticConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[GetChatLegalholdMattersMatterIdFilesResponseDataItem] = (
        _PydanticField(alias="data")
    )
    next_page_token: typing.Optional[str] = _PydanticField(
        alias="next_page_token", default=None
    )
    page_size: typing.Optional[int] = _PydanticField(alias="page_size", default=None)
