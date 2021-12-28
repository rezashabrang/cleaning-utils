"""Types for package."""
from typing import Any, Callable, TypeVar

FunctionType = TypeVar("FunctionType", bound=Callable[..., Any])
