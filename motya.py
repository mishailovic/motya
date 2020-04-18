import os
import random
import time

import typer
from typer import Option, Typer, Argument
from pathlib import Path

from PIL import Image

from motya.font import Font
from motya.motya import Motya
from motya.template import Template, Frame

app = Typer()


@app.command(help="Motya - генератор демотиваторов на python")
def create(
    phrase: Path = Argument(None),
    image: Path = Argument(None),
    template: Path = Option("template.jpg", help="Путь к штаблону демотиватора"),
    images: Path = Option("images/", help="Путь к картинкам для мемов"),
    phrases: Path = Option("phrases.txt", help="Путь к файлу с фразами"),
    font: Path = Option("times.ttf", help="Путь к шрифту"),
    font_size: int = Option(45, help="Размер шрифта, по умолчанию 45"),
    seed: str = Option(time.time(), help="Seed для создания картинки"),
    output: Path = Option("result.png", help="Куда сохранять мем")
):
    print(f"Seed: {seed}")
    random.seed(seed)

    main_template = Template(
        image=Image.open(template),
        width=574,
        height=522,
        frame=Frame(x_start=75, y_start=45, x_end=499, y_end=373),
        padding=10,
    )

    file_list = []
    # noinspection PyTypeChecker
    for dirpath, dirnames, filenames in os.walk(images):
        for filename in [f for f in filenames if f.endswith(("png", "jpg", "jpeg"))]:
            # noinspection PyTypeChecker
            file_list.append(Image.open(os.path.join(images, filename)))

    # noinspection PyTypeChecker
    font = Font(str(font), size=font_size, font_y=390)

    # noinspection PyTypeChecker
    motya = Motya(
        template=main_template,
        phrases=list(open(phrases, encoding="utf-8").readlines()) if phrase is None else [phrase],
        images=list(file_list) if image is None else [Image.open(image)],
        font=font
    )

    output_img = motya.generate()
    output_img.save(output)
    output_img.show()


if __name__ == '__main__':
    app()
