"""Life is fleeting, change is eternal"""

import os
from subprocess import call
import random
import json

wallpaper_dir = '/home/kw/Pictures/Wallpapers'

sublime_settings_dir = "/home/kw/.config/sublime-text-3/Packages/User/Preferences.sublime-settings"
aesthetics = {}

look_me_in_the_eyes = {"wallpaper": "look-me-in-the-eyes.jpeg",
                       "theme": "Flatabulous-dark",
                       "shell-theme": "-1"
                       "sublime-text":
                       {
                           "theme": "Void.sublime-theme",
                           "color-scheme":
                           "Packages/Theme - Freesia/Kalopsia.tmTheme"
                       },
                       "spacemacs":
                       {
                           "theme": "gotham",
                           "transparency": [92, 50]
                       },
                       "dark": 1}

aesthetics["look-me-in-the-eyes"] = look_me_in_the_eyes


# get a list of all the wallpapers
def get_files(dir):
    return os.listdir(dir)


class Aesthetics:

    def __init__(self):
        pass

    @staticmethod
    def change_aesthetic_to(aesthetic):

        wallpaper = "file:///home/kw/Pictures/Wallpapers/" + aesthetic["wallpaper"]
        theme = aesthetic["theme"]
        dark = aesthetic["dark"]

        change_wallpaper_to(wallpaper)
        change_theme_to(theme)
        set_dark_to(dark)


# test
if __name__ == "__main__":
    ls = get_files(wallpaper_dir)
    l = len(ls)
    change_wallpaper_to("look-me-in-the-eyes.jpeg")