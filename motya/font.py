from dataclasses import dataclass


@dataclass
class Font:
    font_filename: str
    size: int
    font_y: int


times = Font(font_filename="times.ttf", size=45, font_y=390)
