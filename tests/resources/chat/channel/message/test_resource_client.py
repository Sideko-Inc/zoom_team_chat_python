"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import Client, AsyncClient
from os import getenv
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_update_204_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.channel.message.update(
        data={
            "method": "pin",
            "message_id": "8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
            "channel_id": "825c9e31f1064c73b394c5e4557d3447",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_update_204_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.channel.message.update(
        data={
            "method": "pin",
            "message_id": "8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
            "channel_id": "825c9e31f1064c73b394c5e4557d3447",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)