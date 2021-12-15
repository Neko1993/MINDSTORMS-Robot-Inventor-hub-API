from typing import Callable, Tuple

TAPPED= 0
DOUBLETAPPED= 1
SHAKE= 2
FREEFALL= 3

def accelerometer(filtered=False) -> Tuple[int, int, int]:
    pass
def gyroscope(filtered=False) -> Tuple[int, int, int]:
    pass
def align_to_model(top: int, front: int) -> None:
    pass
def align_to_model(nsamples: int, callback: Callable[[int], None]) -> None:
    pass
def align_to_model(top: int, front: int, nsamples: int, callback: Callable[[int], None]) -> None:
    pass
def yaw_pitch_roll() -> Tuple[int, int, int]:
    pass
def yaw_pitch_roll(yaw_preset: int) -> None:
    pass
def yaw_pitch_roll(yaw_correction: float) -> None:
    pass
def orientation() -> int:
    pass
def orientation(callback: Callable[[int], None]) -> int:
    pass
def gesture() -> int:
    pass
def gesture(callback: Callable[[int], None]) -> int:
    pass





