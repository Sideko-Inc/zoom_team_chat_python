"""File Generated by Sideko (sideko.dev)"""

import pytest
from zoom_team_chat import Client, AsyncClient
from os import getenv
from pydantic import TypeAdapter
import typing

# test sync & async methods (keep comment for code generation)


def test_create_201_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.im.group.create(
        data={
            "name": "Developers",
            "search_by_account": True,
            "search_by_domain": True,
            "search_by_ma_account": True,
            "type": "normal",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_201_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.im.group.create(
        data={
            "name": "Developers",
            "search_by_account": True,
            "search_by_domain": True,
            "search_by_ma_account": True,
            "type": "normal",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


def test_create_200_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.im.group.create(
        data={
            "name": "Developers",
            "search_by_account": True,
            "search_by_domain": True,
            "search_by_ma_account": True,
            "type": "normal",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_create_200_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.im.group.create(
        data={
            "name": "Developers",
            "search_by_account": True,
            "search_by_domain": True,
            "search_by_ma_account": True,
            "type": "normal",
        }
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


def test_update_204_generated_success_default():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.im.group.update(
        group_id="SobVexyrQjqCkcxjpBWi6w",
        data={
            "name": "Developers",
            "search_by_account": True,
            "search_by_domain": True,
            "search_by_ma_account": True,
            "type": "normal",
        },
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_update_204_generated_success_default():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.im.group.update(
        group_id="SobVexyrQjqCkcxjpBWi6w",
        data={
            "name": "Developers",
            "search_by_account": True,
            "search_by_domain": True,
            "search_by_ma_account": True,
            "type": "normal",
        },
    )
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


def test_get_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.im.group.get(group_id="SobVexyrQjqCkcxjpBWi6w")
    adapter = TypeAdapter(typing.Any)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_get_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.im.group.get(group_id="SobVexyrQjqCkcxjpBWi6w")
    adapter = TypeAdapter(typing.Any)
    adapter.validate_python(response)


def test_list_200_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.im.group.list()
    adapter = TypeAdapter(typing.Dict[str, typing.Any])
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_list_200_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.im.group.list()
    adapter = TypeAdapter(typing.Dict[str, typing.Any])
    adapter.validate_python(response)


def test_delete_204_generated_success():
    """Test description"""
    # tests calling sync method with example data (keep comment for code generation)
    client = Client(token=getenv("API_TOKEN"))
    response = client.im.group.delete(group_id="SobVexyrQjqCkcxjpBWi6w")
    adapter = TypeAdapter(None)
    adapter.validate_python(response)


@pytest.mark.asyncio
async def test_await_delete_204_generated_success():
    """Test description"""
    # tests calling async method with example data (keep comment for code generation)
    client = AsyncClient(token=getenv("API_TOKEN"))
    response = await client.im.group.delete(group_id="SobVexyrQjqCkcxjpBWi6w")
    adapter = TypeAdapter(None)
    adapter.validate_python(response)