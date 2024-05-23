"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import SyncClientWrapper, AsyncClientWrapper
import typing
from zoom_team_chat.utils.request_options import default_request_options, RequestOptions
from zoom_team_chat.types.chat.legalhold.matter.file import models
from zoom_team_chat.utils.query_params import QueryParamTypes, encode_query_param


class FileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def download(
        self,
        *,
        matter_id: str,
        file_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Downloads a zip file.

        **Scopes:** `chat_history_legal_hold:read:admin`,`chat_history_legal_hold:write:admin`

        **Granular Scopes:** `team_chat:read:legal_hold_matter_file:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        _query["file_key"] = encode_query_param(file_key, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="GET",
            path=f"/chat/legalhold/matters/{matter_id}/files/download",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        matter_id: str,
        identifier: str,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatLegalholdMattersMatterIdFilesResponse:
        """
        Returns a list files for given legal hold matter.

        **Scopes:** `chat_history_legal_hold:read:admin`,`chat_history_legal_hold:write:admin`

        **Granular Scopes:** `team_chat:read:list_legal_hold_matter_files:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        _query["identifier"] = encode_query_param(identifier, False)
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="GET",
            path=f"/chat/legalhold/matters/{matter_id}/files",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatLegalholdMattersMatterIdFilesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncFileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def download(
        self,
        *,
        matter_id: str,
        file_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Downloads a zip file.

        **Scopes:** `chat_history_legal_hold:read:admin`,`chat_history_legal_hold:write:admin`

        **Granular Scopes:** `team_chat:read:legal_hold_matter_file:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        _query["file_key"] = encode_query_param(file_key, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="GET",
            path=f"/chat/legalhold/matters/{matter_id}/files/download",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        matter_id: str,
        identifier: str,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatLegalholdMattersMatterIdFilesResponse:
        """
        Returns a list files for given legal hold matter.

        **Scopes:** `chat_history_legal_hold:read:admin`,`chat_history_legal_hold:write:admin`

        **Granular Scopes:** `team_chat:read:list_legal_hold_matter_files:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        _query["identifier"] = encode_query_param(identifier, False)
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="GET",
            path=f"/chat/legalhold/matters/{matter_id}/files",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatLegalholdMattersMatterIdFilesResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
