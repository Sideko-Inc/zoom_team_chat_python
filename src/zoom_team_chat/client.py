"""File Generated by Sideko (sideko.dev)"""

import base64
import httpx
import typing
from zoom_team_chat.environment import Environment
from zoom_team_chat.utils.client_wrapper import SyncClientWrapper, AsyncClientWrapper
from zoom_team_chat.utils.auth import AuthBearer, AuthKeyHeader
from zoom_team_chat.resources.chat import ChatClient, AsyncChatClient
from zoom_team_chat.resources.im import AsyncImClient, ImClient
from zoom_team_chat.resources.contact import AsyncContactClient, ContactClient
from zoom_team_chat.resources.report import ReportClient, AsyncReportClient


class Client:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.PRODUCTION,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        token: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.Client(timeout=timeout) if httpx_client is None else httpx_client
            ),
        )
        if token:
            self.token = token
        elif account_id and client_id and client_secret:
            self.auth_method = "credentials"
            self.account_id = account_id
            self.client_id = client_id
            self.client_secret = client_secret
            self.token = self.get_token_from_credentials()
        else:
            raise ValueError("You must provide either a token or account credentials (account_id, client_id, client_secret).")
        


        # register auth methods (keep comment for code generation)
        self._client_wrapper.register_auth("openapi_oauth", AuthBearer(val=self.token))

        # register sync resources (keep comment for code generation)
        self.chat = ChatClient(client_wrapper=self._client_wrapper)
        self.im = ImClient(client_wrapper=self._client_wrapper)
        self.contact = ContactClient(client_wrapper=self._client_wrapper)
        self.report = ReportClient(client_wrapper=self._client_wrapper)

    def get_token_from_credentials(self):
        oauth_data = {"grant_type": "account_credentials", "account_id": self.account_id}
        auth_str = f"{self.client_id}:{self.client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()
        self._client_wrapper.register_auth(
            "openapi_authorization",
            AuthKeyHeader(header_name="Authorization", val=f"Basic {b64_auth_str}"),
        )
        response = self._client_wrapper.httpx_client.request(
            "POST",
            "https://zoom.us/oauth/token",
            data=oauth_data,
            headers={"Authorization": f"Basic {b64_auth_str}"},
        )
        response = response.json()
        access_token = response.get("access_token")
        if not access_token:
            raise Exception(f"Unable to authenticate with oauth: {response}")
        return access_token

    # register sync api methods (keep comment for code generation)


class AsyncClient:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.PRODUCTION,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        token: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=(
                httpx.AsyncClient(timeout=timeout)
                if httpx_client is None
                else httpx_client
            ),
        )
        if token:
            self.token = token
        elif account_id and client_id and client_secret:
            self.auth_method = "credentials"
            self.account_id = account_id
            self.client_id = client_id
            self.client_secret = client_secret
            self.token = self.get_token_from_credentials()
        else:
            raise ValueError("You must provide either a token or account credentials (account_id, client_id, client_secret).")

        # register auth methods (keep comment for code generation)
        self._client_wrapper.register_auth("openapi_oauth", AuthBearer(val=self.token))
        
        # register async resources (keep comment for code generation)
        self.chat = AsyncChatClient(client_wrapper=self._client_wrapper)
        self.im = AsyncImClient(client_wrapper=self._client_wrapper)
        self.contact = AsyncContactClient(client_wrapper=self._client_wrapper)
        self.report = AsyncReportClient(client_wrapper=self._client_wrapper)

    def get_token_from_credentials(self):
        oauth_data = {"grant_type": "account_credentials", "account_id": self.account_id}
        auth_str = f"{self.client_id}:{self.client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()
        self._client_wrapper.register_auth(
            "openapi_authorization",
            AuthKeyHeader(header_name="Authorization", val=f"Basic {b64_auth_str}"),
        )
        response = self._client_wrapper.httpx_client.request(
            "POST",
            "https://zoom.us/oauth/token",
            data=oauth_data,
            headers={"Authorization": f"Basic {b64_auth_str}"},
        )
        response = response.json()
        access_token = response.get("access_token")
        if not access_token:
            raise Exception(f"Unable to authenticate with oauth: {response}")
        return access_token

    # register async api methods (keep comment for code generation)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: Environment
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Must include a base_url or environment arguments")