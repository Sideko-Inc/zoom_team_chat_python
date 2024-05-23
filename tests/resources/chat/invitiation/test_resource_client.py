"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import Client, AsyncClient
from os import getenv
from zoom_team_chat.types.chat.invitiation import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_join_201_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.invitiation.join(
        data={
            "invite_link": "https://example\.com/invite/123e4567\-e89b\-12d3\-a456\-426614174000"
        }
    )
    adapter = TypeAdapter(models.PostChatInvitationsJoinResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_join_201_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.invitiation.join(
        data={
            "invite_link": "https://example\.com/invite/123e4567\-e89b\-12d3\-a456\-426614174000"
        }
    )
    adapter = TypeAdapter(models.PostChatInvitationsJoinResponse)
    adapter.validate_python(response)


def test_update_invite_link_204_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.invitiation.update_invite_link(
        channel_id="825c9e31f1064c73b394c5e4557d3447"
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_update_invite_link_204_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.invitiation.update_invite_link(
        channel_id="825c9e31f1064c73b394c5e4557d3447"
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


def test_respond_204_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.invitiation.respond(
        data={
            "channel_id": "825c9e31f1064c73b394c5e4557d3447",
            "response": "accept_invitation",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_respond_204_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.invitiation.respond(
        data={
            "channel_id": "825c9e31f1064c73b394c5e4557d3447",
            "response": "accept_invitation",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


def test_get_invite_link_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.invitiation.get_invite_link(
        channel_id="825c9e31f1064c73b394c5e4557d3447"
    )
    adapter = TypeAdapter(models.GetChatInvitationsInviteLinkResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_get_invite_link_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.invitiation.get_invite_link(
        channel_id="825c9e31f1064c73b394c5e4557d3447"
    )
    adapter = TypeAdapter(models.GetChatInvitationsInviteLinkResponse)
    adapter.validate_python(response)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.invitiation.list(
        next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42", page_size=10
    )
    adapter = TypeAdapter(models.GetChatInvitationsResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.invitiation.list(
        next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42", page_size=10
    )
    adapter = TypeAdapter(models.GetChatInvitationsResponse)
    adapter.validate_python(response)