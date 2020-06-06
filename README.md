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

   Уютный чатик в telegram в котором можно скинуть свои красивые демотиваторы, посмеяться вместе над ними и спросить по поводу ошибок: [Ссылка на чат](https://t.me/motyachat)
   
   
   Motya - генератор демотиваторов на python. Все что вам нужно это установить модуль pillow из pip и наслаждаться его работой.

![glaza](result.png)


## 🚀 Установка

   <h3>Для Windows</h3>

   Скачайте установщик с [официального сайта](https://www.python.org/downloads/) и запустите его. Убедитесь, что при установке отметили галочку ![Add Python to PATH](https://user-images.githubusercontent.com/42045258/69171091-557d2780-0b0c-11ea-8adf-7f819357f041.png)
    
   <h3>Для Termux</h3>
   
   ```
   termux-setup-storage
   
   pkg install python clang freetype libjpeg-turbo -y
   
   pip install -r requirements.txt
   
   ```
   <h3>Модуль для юзербота friendly telegram</h3>
   
   Чтобы установить или обновить модуль используйте команду:
   
   ```
   .dlmod https://github.com/mishailovic/motya/raw/master/motyaftg.py
   
   ```
 
 


## Введите следующие команды (для linux в терминал, а на windows в cmd, если на windows пишет что нету git`а, то скачайте программу со вкладки релизов.)

```
git clone https://github.com/mishailovic/motya.git
cd motya
pip3 install -r requirements.txt
```

## 🚩 Запуск

Всё просто! (Предварительно закидываем свои картинки(у) и фразы(у) в соответствующий файл и папку) далее вводим команду `python3 motya.py` или `python motya.py`, и ваш демотиватор готов! По дефолту она берет рандомную картинку из папки images и приделывает к ней рандомный текст из файла phrases.txt, можно кастомизировать работу с помощью флагов, они даны ниже.

### Дока

**Usage**:

```console
$ python motya.py [OPTIONS] [PHRASE] [IMAGE]
```

**Options**:

* `--template PATH`: Путь к шаблону демотиватора
* `--images PATH`: Путь к картинкам для демотиваторов
* `--phrases PATH`: Путь к файлу с фразами
* `--font PATH`: Путь к шрифту
* `--font-size INTEGER`: Размер шрифта, по умолчанию 45
* `--seed TEXT`: Seed для создания картинки
* `--output PATH`: Куда сохранять мем
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

## Поддержка разработчиков

Не забудьте поставить звезду проекту, это - лучшая благодарность :3

Если действительно понравилась программа то я принимаю донаты на Liberapay: https://liberapay.com/mishailovic

## Благодарности

Хочу выразить огромное спасибо всем тем кто работал над этим проектом вместе со мной а именно это:

Code optimization: [Crinny](https://github.com/crinny)

Main code: [Даниил Николаев](https://github.com/nm17)

Inspiration: [Тёма](http://github.com/temaalfer)

FTG module: [Demenkop](https://github.com/demenkop)

Coding and improvements: [rfoxxxy](https://github.com/rfoxxxy)

Фикс зависимостей: [aiexz](https://github.com/aiexz)

Ваш вклад неоценим.


## Stargazers over time

[![Stargazers over time](https://starchart.cc/mishailovic/motya.svg)](https://starchart.cc/mishailovic/motya)
 
