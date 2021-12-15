from typing import Union


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