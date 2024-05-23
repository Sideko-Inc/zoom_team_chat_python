from typing import Union, List, Optional, Mapping, Sequence, Tuple

from urllib.parse import quote_plus

from httpx import QueryParams

PrimitiveData = Optional[Union[str, int, float, bool]]
QueryParamTypes = Union[
    Mapping[str, Union[PrimitiveData, Sequence[PrimitiveData]]],
    List[Tuple[str, PrimitiveData]],
    Tuple[Tuple[str, PrimitiveData], ...],
    str,
    bytes,
]


def encode_query_param(value: QueryParams, explode: bool) -> QueryParamTypes:
    if isinstance(value, (list, dict)) and not explode:
        return quote_plus(",".join(map(str, value)))
    else:
        return value
