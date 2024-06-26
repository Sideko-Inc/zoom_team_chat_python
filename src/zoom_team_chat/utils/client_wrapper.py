# File Generated by Sideko (sideko.dev)
from json import JSONDecodeError
import typing
import pydantic
import httpx
import urllib.parse

from .api_error import ApiError
from .auth import AuthProvider
from .utils import remove_none_from_dict
from .query_params import QueryParamTypes
from .response import from_encodable
from .request_options import RequestOptions
from ..types.binary_response import BinaryResponse

ResponseT = typing.TypeVar(
    "ResponseT",
    bound=typing.Union[
        object,
        str,
        int,
        float,
        None,
        pydantic.BaseModel,
        typing.List[typing.Any],
        typing.Dict[str, typing.Any],
        httpx.Response,
        BinaryResponse,
    ],
)


class BaseClientWrapper:
    def __init__(
        self,
        *,
        base_url: str,
    ):
        self._base_url = base_url
        self._auths: typing.Dict[str, AuthProvider] = {}

    def register_auth(self, auth_id: str, provider: AuthProvider):
        self._auths[auth_id] = provider

    def add_auth_to_request(
        self, auth_names: typing.List[str], **req_kwargs
    ) -> typing.Dict:
        for auth_name in auth_names:
            auth_provider = self._auths.get(auth_name)
            if auth_provider is not None:
                req_kwargs = auth_provider.add_to_request(req_kwargs)
        return req_kwargs

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Sideko-Sdk-Language": "Python",
        }
        return headers

    def get_base_url(self) -> str:
        return self._base_url


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        base_url: str,
        httpx_client: httpx.Client,
    ):
        super().__init__(base_url=base_url)
        self.httpx_client = httpx_client

    def request(
        self,
        method: str,
        path: str,
        cast_to: typing.Type[ResponseT],
        request_options: RequestOptions,
        auth_names: typing.Optional[typing.List[str]] = None,
        query_params: typing.Optional[typing.Dict[str, QueryParamTypes]] = None,
        data: typing.Optional[httpx._types.RequestData] = None,
        files: typing.Optional[httpx._types.RequestFiles] = None,
        json: typing.Optional[typing.Any] = None,
    ) -> ResponseT:
        request = self.add_auth_to_request(
            auth_names or [],
            **{
                "headers": remove_none_from_dict(
                    {
                        **self.get_headers(),
                        **(
                            request_options.get("additional_headers", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                ),
                "params": remove_none_from_dict(
                    {
                        **(query_params or {}),
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                ),
                "data": data,
                "files": files,
                "json": json,
                "timeout": (
                    request_options.get("timeout_in_seconds")
                    if request_options is not None
                    and request_options.get("timeout_in_seconds") is not None
                    else 60
                ),
            },
        )
        request = remove_none_from_dict(request)
        response = self.httpx_client.request(
            method=method,
            url=f"{self._base_url}{path}",
            **request,
            **request_options if request_options is not None else {},
        )
        if 200 <= response.status_code < 300:
            if response.status_code == 204:
                return None
            elif cast_to == BinaryResponse:
                return BinaryResponse(
                    content=response.content, headers=response.headers
                )
            else:
                return from_encodable(data=response.json(), load_with=cast_to)
        else:
            try:
                response_json = response.json()
            except JSONDecodeError:
                raise ApiError(status_code=response.status_code, body=response.text)
            raise ApiError(status_code=response.status_code, body=response_json)


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        base_url: str,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(base_url=base_url)
        self.httpx_client = httpx_client

    async def request(
        self,
        method: str,
        path: str,
        cast_to: typing.Type[ResponseT],
        request_options: RequestOptions,
        auth_names: typing.Optional[typing.List[str]] = None,
        query_params: typing.Optional[typing.Dict[str, QueryParamTypes]] = None,
        data: typing.Optional[httpx._types.RequestData] = None,
        files: typing.Optional[httpx._types.RequestFiles] = None,
        json: typing.Optional[typing.Any] = None,
    ) -> ResponseT:
        request = self.add_auth_to_request(
            auth_names or [],
            **{
                "headers": remove_none_from_dict(
                    {
                        **self.get_headers(),
                        **(
                            request_options.get("additional_headers", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                ),
                "params": remove_none_from_dict(
                    {
                        **(query_params or {}),
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                ),
                "data": data,
                "files": files,
                "json": json,
                "timeout": (
                    request_options.get("timeout_in_seconds")
                    if request_options is not None
                    and request_options.get("timeout_in_seconds") is not None
                    else 60
                ),
            },
        )
        request = remove_none_from_dict(request)
        response = await self.httpx_client.request(
            method=method,
            url=f"{self._base_url}{path}",
            **request,
            **request_options if request_options is not None else {},
        )
        if 200 <= response.status_code < 300:
            if response.status_code == 204:
                return None
            elif cast_to == BinaryResponse:
                return BinaryResponse(
                    content=response.content, headers=response.headers
                )
            else:
                return from_encodable(data=response.json(), load_with=cast_to)
        else:
            try:
                response_json = response.json()
            except JSONDecodeError:
                raise ApiError(status_code=response.status_code, body=response.text)
            raise ApiError(status_code=response.status_code, body=response_json)
