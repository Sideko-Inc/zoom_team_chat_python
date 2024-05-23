"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zoom_team_chat.resources.chat.invitiation.approval.admin import (
    AsyncAdminClient,
    AdminClient,
)
import typing
from zoom_team_chat.utils.request_options import RequestOptions, default_request_options
from zoom_team_chat.types.chat.invitiation.approval import models, params
from zoom_team_chat.utils.query_params import encode_query_param, QueryParamTypes
from zoom_team_chat.utils.request_body import to_encodable


class ApprovalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)
        self.admin = AdminClient(client_wrapper=self._client_wrapper)

    # register sync api methods (keep comment for code generation)
    def respond(
        self,
        *,
        data: typing.Optional[params.PatchChatInvitationsApprovalsBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Approves or denies a channel joining request as channel owner.

        **Scopes:** `chat_channel:write`

        **Granular Scopes:** `team_chat:update:approval`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPatchChatInvitationsApprovalsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="PATCH",
            path="/chat/invitations/approvals",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        channel_id: str,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatInvitationsApprovalsResponse:
        """
        Generates a list of a user's pending approvals to join a channel.

        **Scopes:** `chat_channel:read`,`chat_channel:write`

        **Granular Scopes:** `team_chat:read:list_approvals`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        _query["channel_id"] = encode_query_param(channel_id, False)
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="GET",
            path="/chat/invitations/approvals",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatInvitationsApprovalsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncApprovalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)
        self.admin = AsyncAdminClient(client_wrapper=self._client_wrapper)

    # register async api methods (keep comment for code generation)
    async def respond(
        self,
        *,
        data: typing.Optional[params.PatchChatInvitationsApprovalsBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Approves or denies a channel joining request as channel owner.

        **Scopes:** `chat_channel:write`

        **Granular Scopes:** `team_chat:update:approval`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPatchChatInvitationsApprovalsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="PATCH",
            path="/chat/invitations/approvals",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        channel_id: str,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatInvitationsApprovalsResponse:
        """
        Generates a list of a user's pending approvals to join a channel.

        **Scopes:** `chat_channel:read`,`chat_channel:write`

        **Granular Scopes:** `team_chat:read:list_approvals`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        _query["channel_id"] = encode_query_param(channel_id, False)
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="GET",
            path="/chat/invitations/approvals",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatInvitationsApprovalsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
