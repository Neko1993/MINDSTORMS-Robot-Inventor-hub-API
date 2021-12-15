from typing import Callable


class Button:
    def is_pressed() -> bool:
        pass
    def was_pressed() -> bool:
        pass
    def presses() -> int:
        pass
    def callback(function: Callable[[int], None]) -> None:
        pass

left = Button()
right = Button()
center = Button()
connect = Button()