# import hub.battery, hub.bluetooth, hub.display
from typing import Tuple
import battery, bluetooth, display, button, motion

__all__ = [
        'battery',
        'bluetooth',
        'display',
        'button',
        'motion'
        ]


TOP = 0
FRONT = 1
RIGHT = 2
BOTTOM = 3
BACK = 4
LEFT = 5

__version__ = ''
config = {}
class Image:
    pass

class Image:
    ANGRY= Image('90009:09090:00000:99999:90909:')
    ARROW_E= Image('00900:00090:99999:00090:00900:')
    ARROW_N= Image('00900:09990:90909:00900:00900:')
    ARROW_NE= Image('00999:00099:00909:09000:90000:')
    ARROW_NW= Image('99900:99000:90900:00090:00009:')
    ARROW_S= Image('00900:00900:90909:09990:00900:')
    ARROW_SE= Image('90000:09000:00909:00099:00999:')
    ARROW_SW= Image('00009:00090:90900:99000:99900:')
    ARROW_W= Image('00900:09000:99999:09000:00900:')
    ASLEEP= Image('00000:99099:00000:09990:00000:')
    BUTTERFLY= Image('99099:99999:00900:99999:99099:')
    CHESSBOARD= Image('09090:90909:09090:90909:09090:')
    CLOCK1= Image('00090:00090:00900:00000:00000:')
    CLOCK2= Image('00000:00099:00900:00000:00000:')
    CLOCK3= Image('00000:00000:00999:00000:00000:')
    CLOCK4= Image('00000:00000:00900:00099:00000:')
    CLOCK5= Image('00000:00000:00900:00090:00090:')
    CLOCK6= Image('00000:00000:00900:00900:00900:')
    CLOCK7= Image('00000:00000:00900:09000:09000:')
    CLOCK8= Image('00000:00000:00900:99000:00000:')
    CLOCK9= Image('00000:00000:99900:00000:00000:')
    CLOCK10= Image('00000:99000:00900:00000:00000:')
    CLOCK11= Image('09000:09000:00900:00000:00000:')
    CLOCK12= Image('00900:00900:00900:00000:00000:')
    CONFUSED= Image('00000:09090:00000:09090:90909:')
    COW= Image('90009:90009:99999:09990:00900:')
    DIAMOND= Image('00900:09090:90009:09090:00900:')
    DIAMOND_SMALL= Image('00000:00900:09090:00900:00000:')
    DUCK= Image('09900:99900:09999:09990:00000:')
    FABULOUS= Image('99999:99099:00000:09090:09990:')
    GHOST= Image('99999:90909:99999:99999:90909:')
    GIRAFFE= Image('99000:09000:09000:09990:09090:')
    GO_DOWN= Image('00000:99999:09990:00900:00000:')
    GO_LEFT= Image('00090:00990:09990:00990:00090:')
    GO_RIGHT= Image('09000:09900:09990:09900:09000:')
    GO_UP= Image('00000:00900:09990:99999:00000:')
    HAPPY= Image('00000:09090:00000:90009:09990:')
    HEART= Image('09090:99999:99999:09990:00900:')
    HEART_SMALL= Image('00000:09090:09990:00900:00000:')
    HOUSE= Image('00900:09990:99999:09990:09090:')
    MEH= Image('09090:00000:00090:00900:09000:')
    MUSIC_CROTCHET= Image('00900:00900:00900:99900:99900:')
    MUSIC_QUAVER= Image('00900:00990:00909:99900:99900:')
    MUSIC_QUAVERS= Image('09999:09009:09009:99099:99099:')
    NO= Image('90009:09090:00900:09090:90009:')
    PACMAN= Image('09999:99090:99900:99990:09999:')
    PITCHFORK= Image('90909:90909:99999:00900:00900:')
    RABBIT= Image('90900:90900:99990:99090:99990:')
    ROLLERSKATE= Image('00099:00099:99999:99999:09090:')
    SAD= Image('00000:09090:00000:09990:90009:')
    SILLY= Image('90009:00000:99999:00909:00999:')
    SKULL= Image('09990:90909:99999:09990:09990:')
    SMILE= Image('00000:00000:00000:90009:09990:')
    SNAKE= Image('99000:99099:09090:09990:00000:')
    SQUARE= Image('99999:90009:90009:90009:99999:')
    SQUARE_SMALL= Image('00000:09990:09090:09990:00000:')
    STICKFIGURE= Image('00900:99999:00900:09090:90009:')
    SURPRISED= Image('09090:00000:00900:09090:00900:')
    SWORD= Image('00900:00900:00900:09990:00900:')
    TARGET= Image('00900:09990:99099:09990:00900:')
    TORTOISE= Image('00000:09990:99999:09090:00000:')
    TRIANGLE= Image('00000:00900:09090:99999:00000:')
    TRIANGLE_LEFT= Image('90000:99000:90900:90090:99999:')
    TSHIRT= Image('99099:99999:09990:09990:09990:')
    UMBRELLA= Image('09990:99999:00900:90900:09900:')
    XMAS= Image('00900:09990:00900:09990:99999:')
    YES= Image('00000:00009:00090:90900:09000:')

    ALL_CLOCKS= (Image('00900:00900:00900:00000:00000:'), Image('00090:00090:00900:00000:00000:'), Image('00000:00099:00900:00000:00000:'), Image('00000:00000:00999:00000:00000:'), Image('00000:00000:00900:00099:00000:'), Image('00000:00000:00900:00090:00090:'), Image('00000:00000:00900:00900:00900:'), Image('00000:00000:00900:09000:09000:'), Image('00000:00000:00900:99000:00000:'), Image('00000:00000:99900:00000:00000:'), Image('00000:99000:00900:00000:00000:'), Image('09000:09000:00900:00000:00000:'))
    ALL_ARROWS= (Image('00900:09990:90909:00900:00900:'), Image('00999:00099:00909:09000:90000:'), Image('00900:00090:99999:00090:00900:'), Image('90000:09000:00909:00099:00999:'), Image('00900:00900:90909:09990:00900:'), Image('00009:00090:90900:99000:99900:'), Image('00900:09000:99999:09000:00900:'), Image('99900:99000:90900:00090:00009:'))
    
    def __init__(self, string: str) -> None:
        pass
    
    def init2(self, width: int, height: int) -> None:
        pass
   
    def init3(self, width: int, height: int, buffer: bytes) -> None:
        pass

    def width() -> int:
        pass
    def height() -> int:
        pass
    def shift_left(n: int) -> Image:
        pass
    def shift_right(n: int) -> Image:
        pass
    def shift_up(n: int) -> Image:
        pass
    def shift_down(n: int) -> Image:
        pass
    def get_pixel(x: int, y: int, brightness: int) -> int:
        pass
    def set_pixel(x: int, y: int, brightness: int) -> None:
        pass


def info()->dict:
    pass
def status()->dict:
    pass
def power_off(fast=True, restart=False)->None:
    pass
def power_off(timeout=0)->None:
    pass
def repl_restart(restart: bool) -> None:
    pass
def temperature() -> float:
    pass
def led(color: int) -> None:
    pass
def led(red: int, green: int, blue: int) -> None:
    pass
def led(color: Tuple[int, int, int]) -> None:
    pass
def file_transfer(filename: str, filesize: int, packetsize=1000, timeout=2000, mode=None) -> None:
    pass
