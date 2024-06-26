"""File Generated by Sideko (sideko.dev)"""

from zoom_team_chat.utils.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from zoom_team_chat.resources.report.chat import AsyncChatClient, ChatClient


class ReportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register sync resources (keep comment for code generation)
        self.chat = ChatClient(client_wrapper=self._client_wrapper)

    # register sync api methods (keep comment for code generation)


class AsyncReportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        # register async resources (keep comment for code generation)
        self.chat = AsyncChatClient(client_wrapper=self._client_wrapper)

    # register async api methods (keep comment for code generation)
