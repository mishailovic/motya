from dataclasses import dataclass
from typing import NamedTuple

from PIL.Image import Image


class Dimensions(NamedTuple):
    width: int
    height: int


@dataclass(unsafe_hash=True)
class Frame:
    x_start: int
    y_start: int
    x_end: int
    y_end: int

    @property
    def size(self):
        return Dimensions(self.x_end - self.x_start, self.y_end - self.y_start)

    @property
    def coords(self):
        return self.x_start, self.y_start, self.x_end, self.y_end


@dataclass(unsafe_hash=True, frozen=True)
class Template:
    image: Image
    width: int
    height: int
    frame: Frame
    padding: int
