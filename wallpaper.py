import os
from db_helper import get_list
from PIL import Image, ImageDraw, ImageFont
import gi
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk



# Note: GTK/GDK function details are apparently prone to changing,
# Might want to use QT or wx instead
screen_resolution = Gdk.Monitor.get_workarea(Gdk.Display.get_primary_monitor(Gdk.Display.get_default()))


PATH_TO_IMG = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "img.png")
PATH_TO_FONT = 'Pillow/Tests/fonts/FreeMono.ttf'
FONT_SIZE = 25
FONT_COLOR = (255, 255, 255)
FONT_YOFFSET = 50
FONT_XCOORD = 200
FONT_YCOORD = 35
DIMENSION = (screen_resolution.width, screen_resolution.height)
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
    os.system(
        "/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:" + PATH_TO_IMG)
