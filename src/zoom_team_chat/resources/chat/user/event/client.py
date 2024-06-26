"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zoom_team_chat.types.chat.user.event import params
import typing
from zoom_team_chat.utils.request_options import default_request_options, RequestOptions
from zoom_team_chat.utils.request_body import to_encodable


class EventClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def update_star(
        self,
        *,
        data: typing.Optional[params.PatchChatUsersUserIdEventsBody] = None,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Stars or unstars a contact or channel user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.



        **Scopes:** `chat_event:write`,`chat_event:write:admin`

        **Granular Scopes:** `team_chat:update:chat_control`,`team_chat:update:chat_control:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPatchChatUsersUserIdEventsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="PATCH",
            path=f"/chat/users/{user_id}/events",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncEventClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def update_star(
        self,
        *,
        data: typing.Optional[params.PatchChatUsersUserIdEventsBody] = None,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Stars or unstars a contact or channel user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.



        **Scopes:** `chat_event:write`,`chat_event:write:admin`

        **Granular Scopes:** `team_chat:update:chat_control`,`team_chat:update:chat_control:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPatchChatUsersUserIdEventsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="PATCH",
            path=f"/chat/users/{user_id}/events",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
