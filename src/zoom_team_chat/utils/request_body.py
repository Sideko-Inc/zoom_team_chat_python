from typing import Any, Type
from pydantic import TypeAdapter, BaseModel


def model_dump(item: Any) -> Any:
    if isinstance(item, list):
        return [model_dump(i) for i in item]

    if isinstance(item, BaseModel):
        return item.model_dump(exclude_unset=True, by_alias=True)
    else:
        return item


def to_encodable(*, item: Any, dump_with: Type) -> Any:
    adapter = TypeAdapter(dump_with)
    validated_item = adapter.validate_python(item)
    return model_dump(validated_item)
