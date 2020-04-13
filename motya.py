import os
import random

from PIL import Image, ImageDraw, ImageFont

TEMPLATE_FILENAME = "template.jpg"
PHRASES_FILENAME = "phrases.txt"
IMAGES_DIRECTORY = "images"
EXTENSIONS = [".jpg", ".png"]

RESULT_FILENAME = "result.png"

UPPER_FONT = "times.ttf"
UPPER_SIZE = 45
UPPER_FONT_Y = 390

TEMPLATE_WIDTH = 574
TEMPLATE_HEIGHT = 522
TEMPLATE_COORDS = (75, 45, 499, 373)
PADDING = 10


def is_valid_extension(filename):
    for extension in EXTENSIONS:
        if filename.endswith(extension):
            return True
    return False


def get_random_image():
    file_list = []
    for dirpath, dirnames, filenames in os.walk(IMAGES_DIRECTORY):
        if TEMPLATE_FILENAME in filenames:
            filenames.remove(TEMPLATE_FILENAME)
        for filename in [f for f in filenames if is_valid_extension(f)]:
            file_list.append(os.path.join(IMAGES_DIRECTORY, filename))
    return Image.open(random.choice(file_list))


def get_random_phrase():
    with open(PHRASES_FILENAME) as file:
        content = file.read().splitlines()
    return random.choice(content)


def draw_x_axis_centered_text(image, text, font, size, pos_y):
    draw = ImageDraw.Draw(image)
    text_font = ImageFont.truetype(font, size)
    text_width = text_font.getsize(text)[0]

    while text_width >= TEMPLATE_WIDTH - PADDING * 2:
        text_font = ImageFont.truetype(font, size)
        text_width = text_font.getsize(text)[0]
        size -= 1

    draw.text(((TEMPLATE_WIDTH - text_width) / 2, pos_y), text, font=text_font)


def get_size_from_area(area):
    return area[2] - area[0], area[3] - area[1]


def make_image():
    frame = Image.open(TEMPLATE_FILENAME)
    demot = get_random_image()
    demot = demot.resize(get_size_from_area(TEMPLATE_COORDS), Image.ANTIALIAS)
    frame.paste(demot, TEMPLATE_COORDS)

    draw_x_axis_centered_text(
        frame, get_random_phrase(), UPPER_FONT, UPPER_SIZE, UPPER_FONT_Y
    )

    frame.save(RESULT_FILENAME)
    frame.show()


if __name__ == "__main__":
    make_image()
