"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from zoom_team_chat.utils.request_options import default_request_options, RequestOptions
import typing
from zoom_team_chat.types.chat.channel.member.group import models, params
from zoom_team_chat.utils.request_body import to_encodable


class GroupClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def invite(
        self,
        *,
        data: typing.Optional[params.PostChatChannelsChannelIdMembersGroupsBody] = None,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostChatChannelsChannelIdMembersGroupsResponse:
        """
        Add members and groups to a channel.

        **Scopes:** `chat_channel:write:admin`

        **Granular Scopes:** `team_chat:write:groups:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostChatChannelsChannelIdMembersGroupsBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="POST",
            path=f"/chat/channels/{channel_id}/members/groups",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=models.PostChatChannelsChannelIdMembersGroupsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatChannelsChannelIdMembersGroupsResponse:
        """
        Returns a list of channel member groups.

        **Scopes:** `chat_channel:read:admin`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:read:list_groups:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="GET",
            path=f"/chat/channels/{channel_id}/members/groups",
            auth_names=["openapi_authorization", "openapi_oauth"],
            cast_to=models.GetChatChannelsChannelIdMembersGroupsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self,
        *,
        channel_id: str,
        group_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Removes a group from a chat channel.

        **Scopes:** `chat_channel:write:admin`

        **Granular Scopes:** `team_chat:delete:group:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="DELETE",
            path=f"/chat/channels/{channel_id}/members/groups/{group_id}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncGroupClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)

    # register async api methods (keep comment for code generation)
    async def invite(
        self,
        *,
        data: typing.Optional[params.PostChatChannelsChannelIdMembersGroupsBody] = None,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostChatChannelsChannelIdMembersGroupsResponse:
        """
        Add members and groups to a channel.

        **Scopes:** `chat_channel:write:admin`

        **Granular Scopes:** `team_chat:write:groups:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostChatChannelsChannelIdMembersGroupsBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="POST",
            path=f"/chat/channels/{channel_id}/members/groups",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=models.PostChatChannelsChannelIdMembersGroupsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatChannelsChannelIdMembersGroupsResponse:
        """
        Returns a list of channel member groups.

        **Scopes:** `chat_channel:read:admin`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:read:list_groups:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="GET",
            path=f"/chat/channels/{channel_id}/members/groups",
            auth_names=["openapi_authorization", "openapi_oauth"],
            cast_to=models.GetChatChannelsChannelIdMembersGroupsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self,
        *,
        channel_id: str,
        group_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Removes a group from a chat channel.

        **Scopes:** `chat_channel:write:admin`

        **Granular Scopes:** `team_chat:delete:group:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="DELETE",
            path=f"/chat/channels/{channel_id}/members/groups/{group_id}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
