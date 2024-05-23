"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import AsyncClient, Client
from os import getenv
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_create_204_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.message.reminder.create(
        message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
        data={
            "to_contact": "test@example\.com",
            "to_channel": "cd102f7602c6428db0a273e632eb020B",
            "remind_time": "2024\-02\-10T21:39:50Z",
            "delay_seconds": 1800,
            "reminder_note": "Reminder Note",
        },
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_204_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.message.reminder.create(
        message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
        data={
            "to_contact": "test@example\.com",
            "to_channel": "cd102f7602c6428db0a273e632eb020B",
            "remind_time": "2024\-02\-10T21:39:50Z",
            "delay_seconds": 1800,
            "reminder_note": "Reminder Note",
        },
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


def test_delete_204_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.message.reminder.delete(
        message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
        to_channel="cd102f7602c6428db0a273e632eb020B",
        to_contact="test@example\.com",
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.message.reminder.delete(
        message_id="8cfaf567\-bf5a\-4acc\-b4f2\-88b3d371aca5",
        to_channel="cd102f7602c6428db0a273e632eb020B",
        to_contact="test@example\.com",
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)