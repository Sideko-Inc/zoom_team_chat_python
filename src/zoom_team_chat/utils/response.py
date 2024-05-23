from typing import Any, Union, Dict, Type, TypeVar
from pydantic import BaseModel

T = TypeVar("T", bound=Union[BaseModel, Dict[str, Any]])


def from_encodable(*, data: Any, load_with: Type[T]) -> Any:
    class Caster(BaseModel):
        data: load_with

    return Caster(data=data).data
