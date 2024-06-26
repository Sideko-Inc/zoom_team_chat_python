"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zoom_team_chat.resources.im.user.me.chat.message import (
    MessageClient,
    AsyncMessageClient,
)


class ChatClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)
        self.message = MessageClient(client_wrapper=self._client_wrapper)

    # register sync api methods (keep comment for code generation)


class AsyncChatClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)
        self.message = AsyncMessageClient(client_wrapper=self._client_wrapper)

    # register async api methods (keep comment for code generation)
