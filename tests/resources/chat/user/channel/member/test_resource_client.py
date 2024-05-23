"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import Client, AsyncClient
from os import getenv
from pydantic import TypeAdapter
from zoom_team_chat.types.chat.user.channel.member import models

# test sync & async methods (keep comment for code generation)


def test_invite_201_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.user.channel.member.invite(
        user_id="v4iyWT1LTfy8QvPG4GTvdg",
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        data={"members": [{"email": "jchill@example\.com"}]},
    )
    adapter = TypeAdapter(models.PostChatUsersUserIdChannelsChannelIdMembersResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_invite_201_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.user.channel.member.invite(
        user_id="v4iyWT1LTfy8QvPG4GTvdg",
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        data={"members": [{"email": "jchill@example\.com"}]},
    )
    adapter = TypeAdapter(models.PostChatUsersUserIdChannelsChannelIdMembersResponse)
    adapter.validate_python(response)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.user.channel.member.list(
        user_id="v4iyWT1LTfy8QvPG4GTvdg",
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
        page_size=20,
    )
    adapter = TypeAdapter(models.GetChatUsersUserIdChannelsChannelIdMembersResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.user.channel.member.list(
        user_id="v4iyWT1LTfy8QvPG4GTvdg",
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
        page_size=20,
    )
    adapter = TypeAdapter(models.GetChatUsersUserIdChannelsChannelIdMembersResponse)
    adapter.validate_python(response)


def test_delete_204_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.user.channel.member.delete(
        user_id="v4iyWT1LTfy8QvPG4GTvdg",
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        identifier="jchill@example\.com",
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.user.channel.member.delete(
        user_id="v4iyWT1LTfy8QvPG4GTvdg",
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        identifier="jchill@example\.com",
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)
