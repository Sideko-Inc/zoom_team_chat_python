"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import Client, AsyncClient
from os import getenv
from zoom_team_chat.types.chat.invitiation.approval import models
from pydantic import TypeAdapter

# test sync & async methods (keep comment for code generation)


def test_respond_204_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.invitiation.approval.respond(
        data={
            "channel_id": "825c9e31f1064c73b394c5e4557d3447",
            "invitee_identifier": "zQmgS2TMSpGUOQcXyAHsyA",
            "response": "approve_invitation",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_respond_204_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.invitiation.approval.respond(
        data={
            "channel_id": "825c9e31f1064c73b394c5e4557d3447",
            "invitee_identifier": "zQmgS2TMSpGUOQcXyAHsyA",
            "response": "approve_invitation",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.chat.invitiation.approval.list(
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
        page_size=10,
    )
    adapter = TypeAdapter(models.GetChatInvitationsApprovalsResponse)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.chat.invitiation.approval.list(
        channel_id="825c9e31f1064c73b394c5e4557d3447",
        next_page_token="R4aF9Oj0fVM2hhezJTEmSKaBSkfesDwGy42",
        page_size=10,
    )
    adapter = TypeAdapter(models.GetChatInvitationsApprovalsResponse)
    adapter.validate_python(response)
