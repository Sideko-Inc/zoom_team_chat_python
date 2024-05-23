"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import AsyncClient, Client
from os import getenv
from pydantic import TypeAdapter
from zoom_team_chat.types.chat.channel.member.group import models

# test sync & async methods (keep comment for code generation)


def test_invite_201_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.channel.member.group.invite(
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        data={"groups": [{"group_id": "03dydv46RWKsMzUOdFGdeA"}]},
    )
    adapter = TypeAdapter(models.PostChatChannelsChannelIdMembersGroupsResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_invite_201_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.channel.member.group.invite(
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        data={"groups": [{"group_id": "03dydv46RWKsMzUOdFGdeA"}]},
    )
    adapter = TypeAdapter(models.PostChatChannelsChannelIdMembersGroupsResponse)
    adapter.validate_python(response)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.channel.member.group.list(
        channel_id="825c9e31f1064c73b394c5e4557d3447"
    )
    adapter = TypeAdapter(models.GetChatChannelsChannelIdMembersGroupsResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.channel.member.group.list(
        channel_id="825c9e31f1064c73b394c5e4557d3447"
    )
    adapter = TypeAdapter(models.GetChatChannelsChannelIdMembersGroupsResponse)
    adapter.validate_python(response)


def test_delete_204_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.channel.member.group.delete(
        channel_id="825c9e31f1064c73b394c5e4557d3447", group_id="abc"
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.channel.member.group.delete(
        channel_id="825c9e31f1064c73b394c5e4557d3447", group_id="abc"
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)
