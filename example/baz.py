# pyright: reportImportCycles=false
from typing import Any, TypedDict, Generic, TypeVar
from .foo import Foo
from .bar import Bar

T = TypeVar("T")
U = TypeVar("U")

class BazAttrs(TypedDict, Generic[T, U]):
    pass

class BazOther(TypedDict, Generic[T, U]):
    a: Foo[Any, U]
    b: Bar[Any, U]

Baz = tuple[BazAttrs[T, U], BazOther[T, U]]
