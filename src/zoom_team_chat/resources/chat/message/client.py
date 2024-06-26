"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from zoom_team_chat.resources.chat.message.schedule import (
    AsyncScheduleClient,
    ScheduleClient,
)
from zoom_team_chat.resources.chat.message.reminder import (
    AsyncReminderClient,
    ReminderClient,
)
from zoom_team_chat.resources.chat.message.bookmark import (
    BookmarkClient,
    AsyncBookmarkClient,
)


class MessageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)
        self.schedule = ScheduleClient(client_wrapper=self._client_wrapper)
        self.reminder = ReminderClient(client_wrapper=self._client_wrapper)
        self.bookmark = BookmarkClient(client_wrapper=self._client_wrapper)

    # register sync api methods (keep comment for code generation)


class AsyncMessageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)
        self.schedule = AsyncScheduleClient(client_wrapper=self._client_wrapper)
        self.reminder = AsyncReminderClient(client_wrapper=self._client_wrapper)
        self.bookmark = AsyncBookmarkClient(client_wrapper=self._client_wrapper)

    # register async api methods (keep comment for code generation)
