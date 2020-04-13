from typing import Optional

from PIL import ImageDraw, ImageFont
from PIL.Image import Image

from motya.font import Font, times


class Text:
    def __init__(
        self,
        text: str,
        font: Optional[Font] = times,
        encoding: Optional[str] = "windows-1251",
    ):
        self.text = text
        self.font = font
        self.encoding = encoding

    def draw_x_axis_centered_text(self, image: Image, width: int, padding: int):
        draw = ImageDraw.Draw(image)
        text_font = ImageFont.truetype(self.font.font_filename, self.font.size)
        text_width = text_font.getsize(self.text)[0]

        while text_width >= width - padding * 2:
            text_font = ImageFont.truetype(self.font.font_filename, self.font.size)
            text_width = text_font.getsize(self.text)[0]
            self.font.size -= 1

        draw.text(
            ((width - text_width) / 2, self.font.font_y),
            self.text,
            font=text_font,
        )
        return draw
