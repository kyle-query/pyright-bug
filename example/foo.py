# pyright: reportImportCycles=false
# from __future__ import annotations
from typing import TypedDict, Generic, TypeVar
from .bar import Baz

T = TypeVar("T")
U = TypeVar("U")

class FooAttrs(TypedDict, Generic[T, U]):
    pass

class FooOther(TypedDict, Generic[T, U]):
    a: Baz#[Any, U]

Foo = tuple[FooAttrs[T, U], FooOther[T, U]]
