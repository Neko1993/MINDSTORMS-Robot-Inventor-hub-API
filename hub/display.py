from typing import Callable, Iterable
from hub import Image



def clear():
    pass
def rotation(rotation: int) -> None:
    pass
def align() -> int:
    pass
def align(face: int) -> int:
    pass
def invert() -> bool:
    pass
def invert(invert: bool) -> bool:
    pass
def callback(self, function: Callable[[int], None]) -> None:
    pass
def pixel(x: int, y: int) -> int:
    pass
def pixel(x: int, y: int, brightness: int) -> None:
    pass
def show(image: Image) -> None:
    pass
def show(image: Iterable[Image], delay=400, clear=False, wait=True, loop=False, fade=0) -> None:
    pass