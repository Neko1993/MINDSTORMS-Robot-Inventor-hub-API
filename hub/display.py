from typing import Callable, Iterable, overload
from hub import Image



def clear():
    pass
def rotation(rotation: int) -> None:
    pass
@overload
def align() -> int:
    pass
@overload
def align(face: int) -> int:
    pass
@overload
def invert() -> bool:
    pass
@overload
def invert(invert: bool) -> bool:
    pass
def callback(self, function: Callable[[int], None]) -> None:
    pass
@overload
def pixel(x: int, y: int) -> int:
    print(x, y)
    pass
@overload
def pixel(x: int, y: int, brightness: int) -> None:
    print(x, y, brightness)
    pass
@overload
def show(image) -> None:
    pass
@overload
def show(image, delay=400, clear=False, wait=True, loop=False, fade=0) -> None:
    pass