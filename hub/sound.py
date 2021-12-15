from typing import Callable

SOUND_SIN= 0
SOUND_SQUARE= 1
SOUND_TRIANGLE= 2
SOUND_SAWTOOTH= 3

def volume(volume: int) -> None:
    pass
def volume() -> int:
    pass
def beep(freq=1000, time=1000, waveform=0) -> None:
    pass
def play(filename: str, rate=16000) -> None:
    pass
def callback(self, function: Callable[[int], None]) -> None:
    pass