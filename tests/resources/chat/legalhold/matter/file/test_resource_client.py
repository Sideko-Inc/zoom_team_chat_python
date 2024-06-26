"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import AsyncClient, Client
from os import getenv
from zoom_team_chat.types.chat.legalhold.matter.file import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_download_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.legalhold.matter.file.download(
        matter_id="28c92682\-f4fc\-47b0\-bceb\-14cb839e0279",
        file_key="Zmlyc3QubGFzdEBleGFtcGxlLmNvbS0xNjc5NTg5MjMwNzY4",
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_download_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.legalhold.matter.file.download(
        matter_id="28c92682\-f4fc\-47b0\-bceb\-14cb839e0279",
        file_key="Zmlyc3QubGFzdEBleGFtcGxlLmNvbS0xNjc5NTg5MjMwNzY4",
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.legalhold.matter.file.list(
        matter_id="28c92682\-f4fc\-47b0\-bceb\-14cb839e0279",
        identifier="first\.last@test\.com",
        next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
        page_size=5,
    )
    adapter = TypeAdapter(models.GetChatLegalholdMattersMatterIdFilesResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.legalhold.matter.file.list(
        matter_id="28c92682\-f4fc\-47b0\-bceb\-14cb839e0279",
        identifier="first\.last@test\.com",
        next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
        page_size=5,
    )
    adapter = TypeAdapter(models.GetChatLegalholdMattersMatterIdFilesResponse)
    adapter.validate_python(response)
