"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zoom_team_chat.resources.chat.user.channel.admin import (
    AdminClient,
    AsyncAdminClient,
)
from zoom_team_chat.resources.chat.user.channel.member import (
    AsyncMemberClient,
    MemberClient,
)
from zoom_team_chat.utils.request_options import RequestOptions, default_request_options
import typing
from zoom_team_chat.utils.query_params import encode_query_param, QueryParamTypes
from zoom_team_chat.types.chat.user.channel import models, params
from zoom_team_chat.utils.request_body import to_encodable


class ChannelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)
        self.admin = AdminClient(client_wrapper=self._client_wrapper)
        self.member = MemberClient(client_wrapper=self._client_wrapper)

    # register sync api methods (keep comment for code generation)
    def create(
        self,
        *,
        data: typing.Optional[params.PostChatUsersUserIdChannelsBody] = None,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostChatUsersUserIdChannelsResponse:
        """
        Creates a channel for a user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter. Zoom chat channels allow users to communicate through chat in private or public groups.

        **Scopes:** `chat_channel:write`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:write:user_channel`,`team_chat:write:user_channel:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostChatUsersUserIdChannelsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="POST",
            path=f"/chat/users/{user_id}/channels",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=models.PostChatUsersUserIdChannelsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def update(
        self,
        *,
        data: typing.Optional[params.PatchChatUsersUserIdChannelsChannelIdBody] = None,
        user_id: str,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the name, type, and settings of a specific channel that the user owns or administers. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

        Zoom chat channels allow users to communicate through chat in private or public channels.

        **Scopes:** `chat_channel:write`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:update:user_channel`,`team_chat:update:user_channel:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPatchChatUsersUserIdChannelsChannelIdBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="PATCH",
            path=f"/chat/users/{user_id}/channels/{channel_id}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def get(
        self,
        *,
        user_id: str,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatUsersUserIdChannelsChannelIdResponse:
        """
        Returns information about a specific channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

        Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate through chat in private or public groups.

        **Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:read:user_channel`,`team_chat:read:user_channel:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="GET",
            path=f"/chat/users/{user_id}/channels/{channel_id}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            cast_to=models.GetChatUsersUserIdChannelsChannelIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def list(
        self,
        *,
        user_id: str,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatUsersUserIdChannelsResponseUnion:
        """
        Generates a list of user's chat channels. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate through chat in private or public groups.

        **Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:read:list_user_channels`,`team_chat:read:list_user_channels:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="GET",
            path=f"/chat/users/{user_id}/channels",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatUsersUserIdChannelsResponseUnion,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def delete(
        self,
        *,
        user_id: str,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

        Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate via chat in private or public groups.



        **Scopes:** `chat_channel:write`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:delete:user_channel`,`team_chat:delete:user_channel:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="DELETE",
            path=f"/chat/users/{user_id}/channels/{channel_id}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)

    def batch_delete(
        self,
        *,
        user_id: str,
        channel_ids: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete channels in batches. For user-level apps, pass the `me` value instead of the `userId` parameter.



        **Scopes:** `chat_channel:write`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:delete:channels`,`team_chat:delete:channels:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        _query["channel_ids"] = encode_query_param(channel_ids, False)
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="DELETE",
            path=f"/chat/users/{user_id}/channels",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send sync request (keep comment for code generation)


class AsyncChannelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)
        self.admin = AsyncAdminClient(client_wrapper=self._client_wrapper)
        self.member = AsyncMemberClient(client_wrapper=self._client_wrapper)

    # register async api methods (keep comment for code generation)
    async def create(
        self,
        *,
        data: typing.Optional[params.PostChatUsersUserIdChannelsBody] = None,
        user_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostChatUsersUserIdChannelsResponse:
        """
        Creates a channel for a user. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter. Zoom chat channels allow users to communicate through chat in private or public groups.

        **Scopes:** `chat_channel:write`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:write:user_channel`,`team_chat:write:user_channel:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data, dump_with=params._SerializerPostChatUsersUserIdChannelsBody
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="POST",
            path=f"/chat/users/{user_id}/channels",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=models.PostChatUsersUserIdChannelsResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def update(
        self,
        *,
        data: typing.Optional[params.PatchChatUsersUserIdChannelsChannelIdBody] = None,
        user_id: str,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the name, type, and settings of a specific channel that the user owns or administers. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

        Zoom chat channels allow users to communicate through chat in private or public channels.

        **Scopes:** `chat_channel:write`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:update:user_channel`,`team_chat:update:user_channel:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPatchChatUsersUserIdChannelsChannelIdBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="PATCH",
            path=f"/chat/users/{user_id}/channels/{channel_id}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def get(
        self,
        *,
        user_id: str,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatUsersUserIdChannelsChannelIdResponse:
        """
        Returns information about a specific channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

        Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate through chat in private or public groups.

        **Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:read:user_channel`,`team_chat:read:user_channel:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="GET",
            path=f"/chat/users/{user_id}/channels/{channel_id}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            cast_to=models.GetChatUsersUserIdChannelsChannelIdResponse,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def list(
        self,
        *,
        user_id: str,
        next_page_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GetChatUsersUserIdChannelsResponseUnion:
        """
        Generates a list of user's chat channels. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate through chat in private or public groups.

        **Scopes:** `chat_channel:read`,`chat_channel:write`,`chat_channel:read:admin`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:read:list_user_channels`,`team_chat:read:list_user_channels:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        if next_page_token is not None:
            _query["next_page_token"] = encode_query_param(next_page_token, False)
        if page_size is not None:
            _query["page_size"] = encode_query_param(page_size, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="GET",
            path=f"/chat/users/{user_id}/channels",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=models.GetChatUsersUserIdChannelsResponseUnion,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def delete(
        self,
        *,
        user_id: str,
        channel_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a specific channel. For user-level apps, pass [the `me` value](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#mekeyword) instead of the `userId` parameter.

        Zoom chat [channels](https://support.zoom.us/hc/en-us/articles/200912909-Getting-Started-With-Channels-Group-Messaging-) allow users to communicate via chat in private or public groups.



        **Scopes:** `chat_channel:write`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:delete:user_channel`,`team_chat:delete:user_channel:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`
        """
        # start -- build request data (keep comment for code generation)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="DELETE",
            path=f"/chat/users/{user_id}/channels/{channel_id}",
            auth_names=["openapi_authorization", "openapi_oauth"],
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)

    async def batch_delete(
        self,
        *,
        user_id: str,
        channel_ids: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete channels in batches. For user-level apps, pass the `me` value instead of the `userId` parameter.



        **Scopes:** `chat_channel:write`,`chat_channel:write:admin`

        **Granular Scopes:** `team_chat:delete:channels`,`team_chat:delete:channels:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`
        """
        # start -- build request data (keep comment for code generation)
        _query: typing.Dict[str, QueryParamTypes] = {}
        _query["channel_ids"] = encode_query_param(channel_ids, False)
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="DELETE",
            path=f"/chat/users/{user_id}/channels",
            auth_names=["openapi_authorization", "openapi_oauth"],
            query_params=_query,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)