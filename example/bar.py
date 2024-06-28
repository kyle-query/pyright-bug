# pyright: reportImportCycles=false
# from __future__ import annotations
from typing import TypedDict, Generic, TypeVar
from .baz import Baz

T = TypeVar("T")
U = TypeVar("U")

class BarAttrs(TypedDict, Generic[T, U]):
    pass

class BarOther(TypedDict, Generic[T, U]):
    a: Baz#[Any, U]

Bar = tuple[BarAttrs[T, U], BarOther[T, U]]
