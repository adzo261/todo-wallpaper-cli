import os
import sys
import platform
import ctypes
from PIL import Image, ImageDraw, ImageFont
from db_helper import get_list
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()

PATH_TO_IMG = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "img.png")

PATH_TO_FONT = 'Pillow/Tests/fonts/FreeMono.ttf'
FONT_SIZE = 25
FONT_COLOR = (255, 255, 255)
FONT_YOFFSET = 50
FONT_XCOORD = 200
FONT_YCOORD = 35
DIMENSION = (size.width(), size.height())
WALLPAPER_COLOR = (128, 59, 201)


def set_wallpaper():
    img = Image.new('RGB', DIMENSION, WALLPAPER_COLOR)
    todo_list = get_list()
    if len(todo_list) is not 0:
        i = FONT_YCOORD
        for key, value in todo_list.items():
            d = ImageDraw.Draw(img)
            d.text((FONT_XCOORD, i), key+" : "+value,
                   font=ImageFont.truetype(PATH_TO_FONT, FONT_SIZE), fill=FONT_COLOR)
            i += FONT_YOFFSET
    img.save(PATH_TO_IMG, 'PNG')
    if platform.system() == 'Linux':
        os.system(
            "/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:" + PATH_TO_IMG)
    elif platform.system() == 'Windwos':
        ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH_TO_IMG, 0)
