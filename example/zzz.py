# from __future__ import annotations
from typing import Any, TypedDict, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")

class BarAttrs(TypedDict, Generic[T, U]):
    pass

class BarOther(TypedDict, Generic[T, U]):
    a: "Baz[Any, U]"

Bar = tuple[BarAttrs[T, U], BarOther[T, U]]

class FooAttrs(TypedDict, Generic[T, U]):
    pass

class FooOther(TypedDict, Generic[T, U]):
    a: "Baz[Any, U]"

Foo = tuple[FooAttrs[T, U], FooOther[T, U]]

class BazAttrs(TypedDict, Generic[T, U]):
    pass

class BazOther(TypedDict, Generic[T, U]):
    a: Foo[Any, U]
    b: Bar[Any, U]

Baz = tuple[BazAttrs[T, U], BazOther[T, U]]
