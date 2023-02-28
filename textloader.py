__version__ = "0.1.1"
__author__ = "Suazo-kun (suazokun@gmail.com)"

from threading import Thread
from time import sleep
from sys import platform


class BaseTextLoader:
    _animation: list = []
    _current_animation: int = -1
    _thread: Thread = None
    _animation_delay: float = 0.1
    _stop_animation: bool = False

    @property
    def number_of_characters(self) -> int:
        return len(self._animation)

    @property
    def current_animation(self) -> int:
        return self._current_animation if self._current_animation >= 0 else 0

    @property
    def current_character(self) -> str:
        return self._animation[self.current_animation]

    @property
    def animation_delay(self):
        return self._animation_delay

    @animation_delay.setter
    def animation_delay(self, delay: float):
        if type(delay) != float:
            raise ValueError("delay is not float.")
        else:
            self._animation_delay = delay

    def NextAnimation(self) -> str:
        if self._thread == Thread and self._thread.is_alive():
            return ""

        return self._next_animation()

    def PrintAsyncAnimation(self):
        if (self._thread is None) or (not self._thread.is_alive()):
            self._thread = Thread(
                target=self._print_async_animation, daemon=True)
            self._thread.start()

    def StopAsyncAnimation(self):
        if (type(self._thread) == Thread) and (self._thread.is_alive()):
            self._stop_animation = True
            self._thread.join()
            self._stop_animation = False

    def _next_animation(self):
        if len(self._animation) == 0:
            return ""
        elif self._current_animation == len(self._animation)-1:
            self._current_animation = 0
            return self._animation[self._current_animation]
        else:
            self._current_animation += 1
            return self._animation[self._current_animation]

    def _print_async_animation(self):
        while not self._stop_animation:
            print('\r'+self._next_animation(), end="")
            sleep(self._animation_delay)
        print()


class CirculatePointsLoader(BaseTextLoader):
    _animation = ['⠾', '⠽', '⠻', '⠟', '⠯', '⠷']


class DownPointsLoader(BaseTextLoader):
    _animation = [
        '⠁', '⠂', '⠄', '⡀', '⡈', '⡐', '⡠', '⣀', '⣁', '⣂', '⣄', '⣌', '⣔', '⣤',
        '⣥', '⣦', '⣮', '⣶', '⣷', '⣿', '⣿', '⣿']


class SetPointsLoader(BaseTextLoader):
    _animation = ['⡀', '⡠', '⡢', '⡪', '⡫', '⡻', '⡿', '⣿', '⣿', '⣿']


class RotatePointsLoader(BaseTextLoader):
    _animation = ['⣀', '⡄', '⠆', '⠃', '⠉', '⠘', '⠰', '⢠']
