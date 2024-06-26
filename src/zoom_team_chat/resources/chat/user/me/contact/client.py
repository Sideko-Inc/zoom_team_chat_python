"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import SyncClientWrapper, AsyncClientWrapper
import typing
from zoom_team_chat.utils.request_options import default_request_options, RequestOptions
from zoom_team_chat.types.chat.user.me.contact import models
from zoom_team_chat.utils.query_params import encode_query_param, QueryParamTypes


class ContactClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def get(
        self,
        *,
        identifier: str,
        query_presence_status: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatUsersMeContactsIdentifierResponse:
        """
        Returns information on a specific contact of the Zoom user. A user under an organization's Zoom account has internal users listed under Company Contacts in the Zoom Client. A Zoom user can also add another Zoom user as a [contact](https://support.zoom.us/hc/en-us/articles/115004055706-Managing-Contacts).
        **Note:** This API only supports **user-managed** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app).


        **Scopes:** `chat_contact:read`

        **Granular Scopes:** `team_chat:read:contact`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        if query_presence_status is not None:
            _query["query_presence_status"] = encode_query_param(
                query_presence_status, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="GET",
            path=f"/chat/users/me/contacts/{identifier}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatUsersMeContactsIdentifierResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatUsersMeContactsResponse:
        """
        Lists all the contacts of a Zoom user. Zoom categorizes contacts into **company contacts** and **external contacts**. You must specify the contact type in the `type` query parameter. If you do not specify, by default, the type is set as company contact. A user under an organization's Zoom account has internal users listed under **company contacts** in the Zoom Client. A Zoom user can also add another Zoom user as a [contact](https://support.zoom.us/hc/en-us/articles/115004055706-Managing-Contacts).

        **Note:** This API only supports **user-managed** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app).


        **Scopes:** `chat_contact:read`

        **Granular Scopes:** `team_chat:read:list_contacts`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        if type is not None:
            _query["type"] = encode_query_param(type, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="GET",
            path="/chat/users/me/contacts",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatUsersMeContactsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncContactClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def get(
        self,
        *,
        identifier: str,
        query_presence_status: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatUsersMeContactsIdentifierResponse:
        """
        Returns information on a specific contact of the Zoom user. A user under an organization's Zoom account has internal users listed under Company Contacts in the Zoom Client. A Zoom user can also add another Zoom user as a [contact](https://support.zoom.us/hc/en-us/articles/115004055706-Managing-Contacts).
        **Note:** This API only supports **user-managed** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app).


        **Scopes:** `chat_contact:read`

        **Granular Scopes:** `team_chat:read:contact`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        if query_presence_status is not None:
            _query["query_presence_status"] = encode_query_param(
                query_presence_status, False
            )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="GET",
            path=f"/chat/users/me/contacts/{identifier}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatUsersMeContactsIdentifierResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatUsersMeContactsResponse:
        """
        Lists all the contacts of a Zoom user. Zoom categorizes contacts into **company contacts** and **external contacts**. You must specify the contact type in the `type` query parameter. If you do not specify, by default, the type is set as company contact. A user under an organization's Zoom account has internal users listed under **company contacts** in the Zoom Client. A Zoom user can also add another Zoom user as a [contact](https://support.zoom.us/hc/en-us/articles/115004055706-Managing-Contacts).

        **Note:** This API only supports **user-managed** [OAuth app](https://marketplace.zoom.us/docs/guides/getting-started/app-types/create-oauth-app).


        **Scopes:** `chat_contact:read`

        **Granular Scopes:** `team_chat:read:list_contacts`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        if type is not None:
            _query["type"] = encode_query_param(type, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="GET",
            path="/chat/users/me/contacts",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatUsersMeContactsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
