from typing import Callable, Iterable, Optional, Tuple, Union, overload


class Port:
    class _Device:
        FORMAT_RAW= 0
        FORMAT_PCT= 1
        FORMAT_SI= 2

        def get(format: Optional[int]) -> list:
            pass
        @staticmethod
        @overload
        def mode(mode: int) -> None:
            pass
        @staticmethod
        @overload
        def mode(mode: int, data: bytes) -> None:
            pass
        @staticmethod
        @overload
        def mode(mode: Iterable[Tuple[int, int]]) -> None:
            pass
        @staticmethod
        @overload
        def mode() -> Iterable[Tuple[int, int]]:
            pass
        def pwm(value: int) -> None:
            pass
        def write_direct(data: bytes) -> None:
            pass

    class _Motor(_Device):
        BUSY_MODE= 0
        BUSY_MOTOR= 1
        STOP_FLOAT= 0
        STOP_BRAKE= 1
        STOP_HOLD= 2
        EVENT_COMPLETED= 0
        EVENT_INTERRUPTED= 1
        EVENT_STALLED= 2


        def get(format: Optional[int]) -> list:
            pass
        def mode(mode: Iterable[Tuple[int, int]]) -> None:
            pass
        def pwm(value: int) -> None:
            pass
        def float() -> None:
            pass
        def brake() -> None:
            pass
        def hold() -> None:
            pass
        def busy(type=0) -> bool:
            pass
        @staticmethod
        @overload
        def run_at_speed(speed: int) -> None:
            pass
        @staticmethod
        @overload
        def run_at_speed(speed: int, max_power: int, acceleration: int, deceleration: int, stall: bool) -> None:
            pass
        @staticmethod
        @overload
        def run_for_time(msec: int) -> None:
            pass
        @staticmethod
        @overload
        def run_for_time(msec: int, speed: int, max_power: int, stop: int, acceleration: int, deceleration: int, stall: bool) -> None:
            pass
        @staticmethod
        @overload
        def run_for_degrees(degrees: int) -> None:
            pass
        @staticmethod
        @overload
        def run_for_degrees(degrees: int, speed: int, max_power: int, stop: int, acceleration: int, deceleration: int, stall: bool) -> None:
            pass
        @staticmethod
        @overload
        def run_to_position(position: int) -> None:
            pass
        @staticmethod
        @overload
        def run_to_position(position: int, speed: int, max_power: int, stop: int, acceleration: int, deceleration: int, stall: bool) -> None:
            pass
        def preset(position: int) -> None:
            pass
        def callback(function: Callable[[int], None]) -> None:
            pass
        @staticmethod
        @overload
        def pid() -> tuple:
            pass
        @staticmethod
        @overload
        def pid(p: int, i: int, d: int) -> None:
            pass
        @staticmethod
        @overload
        def default() -> dict:
            pass
        @staticmethod
        @overload
        def default(speed: int, max_power: int, acceleration: int, deceleration: int, stop: int, pid: tuple, stall: bool, callback: Optional[Callable[[int], None]]) -> None:
            pass
        def pair(other_motor: _Motor) -> _MotorPair:
            pass


    class _MotorPair:
        def id() -> int:
            pass
        def primary() -> _Motor:
            pass
        def secondary() -> _Motor:
            pass
        def unpair() -> bool:
            pass
        def float() -> None:
            pass
        def brake() -> None:
            pass
        def hold() -> None:
            pass
        def pwm(pwm_0: int, pwm_1: int) -> None:
            pass
        @overload
        def run_at_speed(speed_0: int, speed_1: int) -> None:
            pass
        @overload
        def run_at_speed(speed_0: int, speed_1: int, max_power: int, acceleration: int, deceleration: int) -> None:
            pass
        @overload
        def run_for_time(msec: int) -> None:
            pass
        @overload
        def run_for_time(msec: int, speed_0: int, speed_1: int, max_power: int, acceleration: int, deceleration: int, stop: int) -> None:
            pass
        @overload
        def run_for_degrees(degrees: int) -> None:
            pass
        @overload
        def run_for_degrees(degrees: int, speed_0: int, speed_1: int, max_power: int, acceleration: int, deceleration: int, stop: int) -> None:
            pass
        @overload
        def run_to_position(position_0: int, position_1: int) -> None:
            pass
        @overload
        def run_to_position(position_0: int, position_1: int, speed: int, max_power: int, acceleration: int, deceleration: int, stop: int) -> None:
            pass
        def preset(position_0: int, position_1: int) -> None:
            pass
        def callback(function: Callable[[int], None]) -> None:
            pass
        def pid(p: int, i: int, d: int) -> None:
            pass
        
    class _Pin:
        def direction(direction: Optional[int]) -> int:
            pass
        def value(value: Optional[int]) -> int:
            pass
    

    device = _Device()
    motor = _Motor()
    p5 = _Pin()
    p6 = _Pin()
    def pwm(value: int) -> None:
        pass
    def callback(function: Callable[[int], None]) -> None:
        pass
    def mode(mode: int, baud_rate=2400) -> None:
        pass
    def info() -> dict:
        pass
    def baud(baud: int) -> None:
        pass
    def read(read: Union[int, any]) -> int:
        pass
    def write(write: bytes) -> int:
        pass

A = Port()
B = Port()
C = Port()
D = Port()
E = Port()
F = Port()   

DETACHED= 0
ATTACHED= 1

MODE_DEFAULT= 0
MODE_FULL_DUPLEX= 1
MODE_HALF_DUPLEX= 2
MODE_GPIO= 3