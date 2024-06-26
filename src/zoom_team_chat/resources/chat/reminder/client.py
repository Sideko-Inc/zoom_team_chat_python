"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import SyncClientWrapper, AsyncClientWrapper
import typing
from zoom_team_chat.utils.request_options import default_request_options, RequestOptions
from zoom_team_chat.types.chat.reminder import models
from zoom_team_chat.utils.query_params import QueryParamTypes, encode_query_param


class ReminderClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def list(
        self,
        *,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        to_channel: typing.Optional[str] = None,
        to_contact: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatReminderResponse:
        """
        Returns a list reminders for a person or a chat channel.

        **Scopes:** `chat_message:read`,`chat_message:read:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        if to_channel is not None:
            _query["to_channel"] = encode_query_param(to_channel, False)
        if to_contact is not None:
            _query["to_contact"] = encode_query_param(to_contact, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="GET",
            path="/chat/reminder",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatReminderResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncReminderClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def list(
        self,
        *,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        to_channel: typing.Optional[str] = None,
        to_contact: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatReminderResponse:
        """
        Returns a list reminders for a person or a chat channel.

        **Scopes:** `chat_message:read`,`chat_message:read:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        if to_channel is not None:
            _query["to_channel"] = encode_query_param(to_channel, False)
        if to_contact is not None:
            _query["to_contact"] = encode_query_param(to_contact, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="GET",
            path="/chat/reminder",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatReminderResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
