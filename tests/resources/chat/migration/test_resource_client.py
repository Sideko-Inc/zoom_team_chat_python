"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import Client, AsyncClient
from os import getenv
from pydantic import TypeAdapter
from zoom_team_chat.types.chat.migration import models

# test sync & async methods (keep comment for code generation)


def test_migrate_messages_201_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.migration.migrate_messages(
        data={
            "messages": [
                {
                    "message_timestamp": 1679589230768,
                    "sender": "649ad5f12f804cfea7dd7b1c1bb4c337",
                    "to_channel": "825c9e31f1064c73b394c5e4557d3447",
                    "to_contact": "jchill@example\.com",
                    "message": "Hello",
                    "file_ids": ["M87v\-bbmRGKCtl8nGNggvA"],
                    "reply_main_message_id": "27ED2949\-6457\-417C\-83EA\-72515DAF00BD",
                    "reply_main_message_timestamp": 1679589230768,
                }
            ]
        }
    )
    adapter = TypeAdapter(models.PostChatMigrationMessagesResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_migrate_messages_201_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.migration.migrate_messages(
        data={
            "messages": [
                {
                    "message_timestamp": 1679589230768,
                    "sender": "649ad5f12f804cfea7dd7b1c1bb4c337",
                    "to_channel": "825c9e31f1064c73b394c5e4557d3447",
                    "to_contact": "jchill@example\.com",
                    "message": "Hello",
                    "file_ids": ["M87v\-bbmRGKCtl8nGNggvA"],
                    "reply_main_message_id": "27ED2949\-6457\-417C\-83EA\-72515DAF00BD",
                    "reply_main_message_timestamp": 1679589230768,
                }
            ]
        }
    )
    adapter = TypeAdapter(models.PostChatMigrationMessagesResponse)
    adapter.validate_python(response)


def test_migrate_reactions_204_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.migration.migrate_reactions(
        data={
            "reactions": [
                {
                    "message_id": "1679113305154",
                    "message_timestamp": 1679113305154,
                    "to_channel": "825c9e31f1064c73b394c5e4557d3447",
                    "to_contact": "jchill@example\.com",
                    "emojis": [
                        {
                            "emoji": "\+U1F400",
                            "user_identifier": ["649ad5f12f804cfea7dd7b1c1bb4c337"],
                        }
                    ],
                }
            ]
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_migrate_reactions_204_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.migration.migrate_reactions(
        data={
            "reactions": [
                {
                    "message_id": "1679113305154",
                    "message_timestamp": 1679113305154,
                    "to_channel": "825c9e31f1064c73b394c5e4557d3447",
                    "to_contact": "jchill@example\.com",
                    "emojis": [
                        {
                            "emoji": "\+U1F400",
                            "user_identifier": ["649ad5f12f804cfea7dd7b1c1bb4c337"],
                        }
                    ],
                }
            ]
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)