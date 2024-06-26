"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zoom_team_chat.types.chat.migration.user.event import params
import typing
from zoom_team_chat.utils.request_options import default_request_options, RequestOptions
from zoom_team_chat.utils.request_body import to_encodable


class EventClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)

    # register sync api methods (keep comment for code generation)
    def migrate(
        self,
        *,
        data: typing.Optional[params.PostChatMigrationUsersIdentifierEventsBody] = None,
        identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Performs operations on migrated 1:1 conversations or channels. For now, the only supported operation is to star 1:1 conversations or channels.

        **Note**: By default, the use of this endpoint is **locked**. We make it available upon request on a case by case basis. To unlock this endpoint, contact [Zoom Support](https://support.zoom.com/hc/en/contact?id=contact_us).

        **Scopes:** `chat_migration:write:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostChatMigrationUsersIdentifierEventsBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send sync request (keep comment for code generation)
        return self._client_wrapper.request(
            method="POST",
            path=f"/chat/migration/users/{identifier}/events",
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
    async def migrate(
        self,
        *,
        data: typing.Optional[params.PostChatMigrationUsersIdentifierEventsBody] = None,
        identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Performs operations on migrated 1:1 conversations or channels. For now, the only supported operation is to star 1:1 conversations or channels.

        **Note**: By default, the use of this endpoint is **locked**. We make it available upon request on a case by case basis. To unlock this endpoint, contact [Zoom Support](https://support.zoom.com/hc/en/contact?id=contact_us).

        **Scopes:** `chat_migration:write:admin`

        **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`
        """
        # start -- build request data (keep comment for code generation)
        _json = to_encodable(
            item=data,
            dump_with=params._SerializerPostChatMigrationUsersIdentifierEventsBody,
        )
        # end -- build request data (keep comment for code generation)

        # start -- send async request (keep comment for code generation)
        return await self._client_wrapper.request(
            method="POST",
            path=f"/chat/migration/users/{identifier}/events",
            auth_names=["openapi_authorization", "openapi_oauth"],
            json=_json,
            cast_to=None,
            request_options=request_options or default_request_options(),
        )
        # end -- send async request (keep comment for code generation)
