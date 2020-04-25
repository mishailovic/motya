# Адаптированная версия Моти для Friendly-Telegram

# Оптимизирован и создан для Heroku

import logging
import os
import io
import requests
from PIL import Image, ImageDraw, ImageFont
from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(Motya())


class Motya(loader.Module):
    """Простой и крутой (\U0001F60E) генератор демотиваторов.
Чат и помощь в @motyachat"""

    strings = {
        'name': 'Motya',
        'er_type': ('<code>Тип файла не поддерживается, используйте  '
                    'фото или стикеры</code>'),
        'er_template': ('<code>Произошла ошибка на этапе '
                        'получения темплейта.'
                        ' Подробнее в логе</code>'),
        'er_font': ('<code>Шрифт сказал идти подальше. '
                    'Подробнее в логе</code>'),
        'usage': '<code>.help Motya</code> для помощи',
        'upper_size_cfg_doc': 'Размер шрифта',
        'upper_font_y_cfg_doc': 'Расположение шрифта по вертикали',
        'template_width_cfg_doc': ('Расположение шрифта по горизонтали'
                                   ' (хз почему шрифта лол)'),
        'template_coords_cfg_doc': 'Координаты темплейта',
        'padding_cfg_doc': 'Размеры отступов(padding)'
    }

    def __init__(self):
        self.config = loader.ModuleConfig("upper_size", 45,
                                          lambda: self.strings['upper_size_cfg_doc'],  # noqa: E501
                                          "upper_font_y", 390,
                                          lambda: self.strings['upper_font_y_cfg_doc'],  # noqa: E501
                                          "template_width", 574,
                                          lambda: self.strings['template_width_cfg_doc'],  # noqa: E501
                                          "template_coords", (75, 45, 499,
                                                              373),
                                          lambda: self.strings['template_coords_cfg_doc'],  # noqa: E501
                                          "padding", 10,
                                          lambda: self.strings['padding_cfg_doc'])  # noqa: E501

        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
        self.prename = "premotya.png"
        self.mot_template = 'template.jpg'
        self.upper_font = 'times.ttf'

    async def client_ready(self, client, db):
        self._db = db
        self.client = client
        self._me = await client.get_me()

    async def motyacmd(self, message):
        """Ответьте текстом на картинку или стикер для получения демотиватора"""  # noqa: E501

        # Скачивание
        # TODO: Поменять скачивание на использование байтов(запрещено ФТГ)
        try:
            url = 'https://raw.githubusercontent.com/mishailovic/motya-cli/master/template.jpg'  # noqa: E501
            r = requests.get(url, allow_redirects=True)
            open('template.jpg', 'wb').write(r.content)
        except Exception as e:
            logger.error(e, exc_info=True)
            await utils.answer(message, self.strings['er_template'])

        try:
            url2 = 'https://github.com/mishailovic/motya-cli/blob/master/times.ttf?raw=true'  # noqa: E501
            r2 = requests.get(url2, allow_redirects=True)
            open('times.ttf', 'wb').write(r2.content)
        except Exception as e:
            logger.error(e, exc_info=True)
            await utils.answer(message, self.strings['er_font'])

        # Аргументики
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings['usage'])
            return

        # Сохранение файла
        img = await message.get_reply_message()
        if img and img.media:
            photo = io.BytesIO()
            await self.client.download_media(img, photo)
        else:
            await utils.answer(message, self.strings['usage'])
            return

        if photo:
            try:
                image = Image.open(photo)
            except OSError:
                await utils.answer(message, self.strings['er_type'])
                return
            image.save(self.prename, "PNG")
            image.close()

        # Собственно Мотя
        def draw_x_axis_centered_text(image, text, font, size, pos_y):
            draw = ImageDraw.Draw(image)
            text_font = ImageFont.truetype(font, size)
            text_width = text_font.getsize(text)
            while text_width[0] >= self.config['template_width'] - self.config['padding'] * 2:  # noqa: E501
                text_font = ImageFont.truetype(font, size)
                text_width = text_font.getsize(text)
                size -= 1
            draw.text(((self.config['template_width'] - text_width[0]) / 2,
                      pos_y),
                      text,
                      font=text_font)

        def get_size_from_area(area):
            return area[2] - area[0], area[3] - area[1]

        def make_image():
            frame = Image.open(self.mot_template)
            demot = Image.open(self.prename)
            demot = demot.resize(get_size_from_area(self.config['template_coords']),  # noqa: E501
                                 Image.ANTIALIAS)
            frame.paste(demot, self.config['template_coords'])
            draw_x_axis_centered_text(frame,
                                      args,
                                      self.upper_font,
                                      self.config['upper_size'],
                                      self.config['upper_font_y'])
            img = io.BytesIO()
            img.name = 'motya.png'
            frame.save(img, 'PNG')
            return img

        # Отправка

        demot = make_image()
        demot.seek(0)
        await utils.answer(message, demot)

        if os.path.isfile(self.prename):
            os.remove(self.prename)
        if os.path.isfile(self.mot_template):
            os.remove(self.mot_template)
        if os.path.isfile(self.upper_font):
            os.remove(self.upper_font)
