"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import AsyncClient, Client
from os import getenv
from zoom_team_chat.types.chat.channel.pinned import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.channel.pinned.list(
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        include_history=False,
        next_page_token="1707034615202",
        page_size=10,
    )
    adapter = TypeAdapter(models.GetChatChannelsChannelIdPinnedResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.channel.pinned.list(
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        include_history=False,
        next_page_token="1707034615202",
        page_size=10,
    )
    adapter = TypeAdapter(models.GetChatChannelsChannelIdPinnedResponse)
    adapter.validate_python(response)