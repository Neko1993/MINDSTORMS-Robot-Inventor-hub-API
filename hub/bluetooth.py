from typing import Callable

def discoverable() -> int:
    pass
def discoverable(time: int) -> None:
    pass
def info() -> dict:
    pass
def forget(address) -> bool:
    pass
def lwp_advertise() -> int:
    pass
def lwp_advertise(timeout: int) -> None:
    pass
def lwp_bypass() -> bool:
    pass
def lwp_bypass(bypass: bool) -> None:
    pass
def lwp_monitor(self, handler: Callable[[int], None]) -> None:
    pass
