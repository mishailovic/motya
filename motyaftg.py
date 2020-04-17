# Адаптированная версия Моти для Friendly-Telegram

# Оптимизирован и создан для Heroku

import logging
import os
import io
import requests
from PIL import Image, ImageDraw, ImageFont
from .. import loader, utils

from userbot import bot

logger = logging.getLogger(__name__)

def register(cb):
    cb(Motya())

class Motya(loader.Module):
    """Простой и крутой (\U0001F60E) генератор демотиваторов.
Чат и помощь в @motyachat"""
    # Сообщения
    messages = {
    'init': '<code>Подготовка Моти)</code>',
    'usage': '<code>.help Motya</code> для помощи',
    'processing': '<code>Обработка...</code>',
    'er_type': '<code>Тип файла не поддерживается, используйте фото или стикеры</code>',
    'er_template': '<code>Произошла ошибка на этапе получения темплейта</code>',
    'er_font': '<code>Шрифт сказал идти подальше</code>',
    'er_send': '<code>Ошибка при отправке(</code>',
    'processing1': '<code>Обработка..</code>'
    }

    def __init__(self):
        self.name = _("Motya")
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self._me = await client.get_me()

    async def motyacmd(self, message):
        """Ответьте текстом на картинку или стикер для получения демотиватора"""

        # Переменные
        prename = "premotya.png"
        name = "motya.png"
        mot_template = 'template.jpg'
        UPPER_FONT = 'times.ttf'
        UPPER_SIZE = 45
        UPPER_FONT_Y = 390
        TEMPLATE_WIDTH = 574
        TEMPLATE_HEIGHT = 522
        TEMPLATE_COORDS = (75, 45, 499, 373)
        PADDING = 10

        # Удаление предыдущих файлов, если таковые присутствуют
        if os.path.isfile(prename): os.remove(prename)
        if os.path.isfile(name): os.remove(name)
        if os.path.isfile(mot_template): os.remove(mot_template)
        if os.path.isfile(UPPER_FONT): os.remove(UPPER_FONT)

        # Скачивание
        await message.edit(_(self.messages['init']))
        try:
            url = 'https://raw.githubusercontent.com/mishailovic/motya-cli/master/template.jpg'
            r = requests.get(url, allow_redirects=True)
            open('template.jpg', 'wb').write(r.content)
        except:
            await message.edit(_(self.messages['er_template']))

        try:
            url2 = 'https://github.com/mishailovic/motya-cli/blob/master/times.ttf?raw=true'
            r2 = requests.get(url2, allow_redirects=True)
            open('times.ttf', 'wb').write(r2.content)
        except:
            await message.edit(_(self.messages['er_font']))

        # Аргументики
        args = utils.get_args_raw(message)
        if not args:
            await message.edit(_(self.messages['usage']))
            return

        # Сохранение файла
        img = await message.get_reply_message()
        if img and img.media:
            photo = io.BytesIO()
            await bot.download_media(img, photo)
        else:
            await message.edit(_(self.messages['usage']))
            return

        if photo:
            await message.edit(_(self.messages['processing']))
            try:
                image = Image.open(photo)
            except OSError:
                await message.edit(_(self.messages['er_type']))
                return
            image.save(prename, "PNG")
            image.close()
            await message.edit(_(self.messages['processing1']))

        # Собственно Мотя
        def draw_x_axis_centered_text(image, text, font, size, pos_y):
            draw = ImageDraw.Draw(image)
            text_font = ImageFont.truetype(font, size)
            text_width, text_baseline = text_font.getsize(text)
            while text_width >= TEMPLATE_WIDTH - PADDING * 2:
                text_font = ImageFont.truetype(font, size)
                text_width, text_baseline = text_font.getsize(text)
                size -= 1
            draw.text(((TEMPLATE_WIDTH - text_width) / 2, pos_y), text, font=text_font)

        def get_size_from_area(area):
            return area[2] - area[0], area[3] - area[1]

        def make_image():
            frame = Image.open(mot_template)
            demot = Image.open(prename)
            demot = demot.resize(get_size_from_area(TEMPLATE_COORDS), Image.ANTIALIAS)
            frame.paste(demot, TEMPLATE_COORDS)
            draw_x_axis_centered_text(frame, args, UPPER_FONT, UPPER_SIZE, UPPER_FONT_Y)
            frame.save(name, "PNG")

        # Отправка
        make_image()
        await message.edit(_(self.messages['processing']))
        try:
            await img.client.send_file(entity = await img.client.get_input_entity(img.chat_id), file=name)
        except:
            await message.edit(_("<code>Ошибка при отправке(</code>"))
        await message.delete()

        # ещё одна чистка
        if os.path.isfile(prename): os.remove(prename)
        if os.path.isfile(name): os.remove(name)
        if os.path.isfile(mot_template): os.remove(mot_template)
        if os.path.isfile(UPPER_FONT): os.remove(UPPER_FONT)
