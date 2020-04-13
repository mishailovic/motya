import random
from typing import List, Optional

from PIL.Image import Image, ANTIALIAS

from motya.font import Font, times
from motya.template import Template
from motya.text import Text


class Motya:
    def __init__(
        self,
        template: Template,
        phrases: Optional[List[str]] = None,
        images: Optional[List[Image]] = None,
    ):
        self.template = template
        self.phrases = phrases
        self.images = images

    @property
    def random_phrase(self):
        return random.choice(self.phrases) if self.phrases is not None else None

    @property
    def random_image(self):
        return random.choice(self.images)

    def generate(
        self,
        phrase: Optional[str] = None,
        image: Optional[Image] = None,
        font: Optional[Font] = times,
    ):
        template_image = self.template.image

        demotivator_image = self.random_image.resize(
            self.template.frame.size, ANTIALIAS
        )
        template_image.paste(demotivator_image, self.template.frame.coords)

        image = Text(phrase or self.random_phrase, font).draw_x_axis_centered_text(
            self.template.image, self.template.width, padding=self.template.padding
        )

        return template_image
