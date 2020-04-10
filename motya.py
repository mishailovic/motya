import PIL, os
from PIL import Image, ImageDraw, ImageFont
import random

TEMPLATE_FILENAME = 'template.jpg'
PHRASES_FILENAME = 'phrases.txt'
IMAGES_DIRECTORY = 'images'
EXTENSIONS = ['.jpg', '.png']

RESULT_FILENAME = 'result.png'

UPPER_FONT = 'times.ttf'
UPPER_SIZE = 45
UPPER_FONT_Y = 390

TEMPLATE_WIDTH = 574
TEMPLATE_HEIGHT = 522
TEMPLATE_COORDS = (75, 45, 499, 373)
PADDING = 10

def isValidExtension(filename):
    for extension in EXTENSIONS:
        if filename.endswith(extension):
            return True
    return False

def getRandomImage():
    fileList = []
    for dirpath, dirnames, filenames in os.walk(IMAGES_DIRECTORY):
        if TEMPLATE_FILENAME in filenames: filenames.remove(TEMPLATE_FILENAME)
        for filename in [f for f in filenames if isValidExtension(f)]:
            fileList.append(os.path.join(IMAGES_DIRECTORY, filename))
    return PIL.Image.open(random.choice(fileList))

def getRandomPhrase():
    with open(PHRASES_FILENAME) as file:
        content = file.read().splitlines()
    return random.choice(content)

def drawXAxisCenteredText(image, text, font, size, pos_y):
    draw = ImageDraw.Draw(image)
    textFont = ImageFont.truetype(font, size)
    textWidth = textFont.getsize(text)[0]

    while textWidth >= TEMPLATE_WIDTH - PADDING * 2:
        textFont = ImageFont.truetype(font, size)
        textWidth = textFont.getsize(text)[0]
        size -= 1
    
    draw.text(((TEMPLATE_WIDTH - textWidth) / 2, pos_y), text, font = textFont)

def getSizeFromArea(area):
    return (area[2] - area[0], area[3] - area[1])

def makeImage():
    frame = PIL.Image.open(TEMPLATE_FILENAME)
    demot = getRandomImage()
    demot = demot.resize(getSizeFromArea(TEMPLATE_COORDS), PIL.Image.ANTIALIAS)
    frame.paste(demot, TEMPLATE_COORDS)

    drawXAxisCenteredText(frame, getRandomPhrase(),
                          UPPER_FONT, UPPER_SIZE,
                          UPPER_FONT_Y)
    
    frame.save(RESULT_FILENAME)
    frame.show()

if __name__ == '__main__':
    makeImage()
