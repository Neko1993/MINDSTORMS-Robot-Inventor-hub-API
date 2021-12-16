from typing import Callable, overload

@overload
def discoverable() -> int:
    pass
@overload
def discoverable(time: int) -> None:
    pass
def info() -> dict:
    pass
def forget(address) -> bool:
    pass
@overload
def lwp_advertise() -> int:
    pass
@overload
def lwp_advertise(timeout: int) -> None:
    pass
@overload
def lwp_bypass() -> bool:
    pass
@overload
def lwp_bypass(bypass: bool) -> None:
    pass
def lwp_monitor(self, handler: Callable[[int], None]) -> None:
    pass
