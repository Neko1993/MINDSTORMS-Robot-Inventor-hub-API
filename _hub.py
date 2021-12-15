from typing import Callable, Iterable, Tuple, Union

class battery:
    BATTERY_NO_ERROR= 0
    BATTERY_HUB_TEMPERATURE_CRITICAL_OUT_OF_RANGE= -1
    BATTERY_TEMPERATURE_OUT_OF_RANGE= -2
    BATTERY_TEMPERATURE_SENSOR_FAIL= -3
    BATTERY_BAD_BATTERY= -4
    BATTERY_VOLTAGE_TOO_LOW= -5
    BATTERY_MISSING= -6

    USB_CH_PORT_NONE= 0
    USB_CH_PORT_SDP= 1
    USB_CH_PORT_CDP= 2
    USB_CH_PORT_DCP= 3

    CHARGER_STATE_FAIL= -1
    CHARGER_STATE_DISCHARGING= 0
    CHARGER_STATE_CHARGING_ONGOING= 1
    CHARGER_STATE_CHARGING_COMPLETED= 2

    def voltage()-> int:
        pass

    def current() -> int:
        pass

    def capacity_left() -> int:
        pass

    def temperature() -> float:
        pass

    def charger_detect() -> Union[bool, int]:
        pass

    def info() -> dict:
        pass

class bluethooth:
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

class button:
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

class display:
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
