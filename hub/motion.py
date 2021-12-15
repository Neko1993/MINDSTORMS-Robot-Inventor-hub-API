from typing import Callable, Tuple, overload

TAPPED= 0
DOUBLETAPPED= 1
SHAKE= 2
FREEFALL= 3

def accelerometer(filtered=False) -> Tuple[int, int, int]:
    pass
def gyroscope(filtered=False) -> Tuple[int, int, int]:
    pass
@overload
def align_to_model(top: int, front: int) -> None:
    pass
@overload
def align_to_model(nsamples: int, callback: Callable[[int], None]) -> None:
    pass
@overload
def align_to_model(top: int, front: int, nsamples: int, callback: Callable[[int], None]) -> None:
    pass
@overload
def yaw_pitch_roll() -> Tuple[int, int, int]:
    pass
@overload
def yaw_pitch_roll(yaw_preset: int) -> None:
    pass
@overload
def yaw_pitch_roll(yaw_correction: float) -> None:
    pass
@overload
def orientation() -> int:
    pass
@overload
def orientation(callback: Callable[[int], None]) -> int:
    pass
@overload
def gesture() -> int:
    pass
@overload
def gesture(callback: Callable[[int], None]) -> int:
    pass





