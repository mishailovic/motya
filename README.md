<h1 align="center">Motya</h1>
<p align="center">
    Открытая и бесплатная утилита для генерации демотиваторов.
    <br /><br />
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white">
    <img alt="Repo size" src="https://img.shields.io/github/repo-size/mishailovic/motya">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    <img alt="issues" src="https://img.shields.io/github/issues/mishailovic/motya">
    <img alt="release" src="https://img.shields.io/github/v/release/mishailovic/motya">
</p>

   Motya - генератор демотиваторов на python. Все что вам нужно это установить модуль pillow из pip и наслаждаться его работой. Берет рандомную картинку из папки "images" и прилепляет на нее рандомный текст из файла "phrases.txt" (Если в папке и в файле только одна картинка и один текст, то будет использовать только их. Сохраняет готовое изображение в файл result.png, если таковой уже есть - то перезаписывает. Наслаждайтесь.

![crinny](result.png)


## 🚀 Установка

   <h3>Для Windows</h3>

   Просто скачайте последний релиз из вкладки [релизов](https://github.com/mishailovic/motya/releases)
    

   <h3>Для Android</h3>

   Установите приложение [Termux](https://play.google.com/store/apps/details?id=com.termux), запустите его и введите следующие команды поочерёдно:
     ```sh
     pkg install python
     ```

## Введите следующие команды (только для termux и linux) ([куда?](http://comp-profi.com/kak-vyzvat-komandnuyu-stroku-ili-konsol-windows/)):

```sh
git clone https://github.com/mishailovic/motya.git
cd motya
pip3 intsall pillow
```

## 🚩 Запуск

Всё просто! (Предварительно закидываем свои картинки(у) и фразы(у) в соответствующий файл и папку) далее вводим команду `python3 motya.py` или `python motya.py`, если на Windows, то запускаем файл motya.exe и ваш демотиватор готов!
 
