"""The main elements making up the "look" or aesthetic of the linux pc are:

  * Wallpaper
  * Theme
  * Shell Theme
  * Icons
  * Terminal Profile
  * Terminal Transparency
  * Text Editor Themes/Color Schemes
"""

import json
import sys
from gtk import GTKAesthetic
from sublime import SublimeAesthetic


class AestheticMissingError(Exception):
    """Define a custom error for when the Aesthetic
    file is not found"""
    pass


def fetch(filename):

    try:
        with open(filename, "r+") as f:
            data = json.load(f)
    except IOError:
        data = {}

    return data


class Aesthetic:
    """
        Nothing's perfect, the world's not perfect.
        But it's there for us, trying the best it can;
        that's what makes it so damn beautiful.
    """

    def __init__(self, filename):

        try:
            data = fetch(filename)
            if data == {}:
                raise AestheticMissingError

            gtk = GTKAesthetic(data)
            subl = SublimeAesthetic(data)

        except AestheticMissingError:
            print("Error: Aesthetic file not found")

        else:

            """GnomeTookKit changes"""
            gtk.change_wallpaper()
            gtk.change_theme()
            gtk.change_shell_theme()
            gtk.change_icon_theme

            """Sublime text changes"""
            subl.change_theme()
            subl.change_color_scheme()
            subl.add_custom_pairs()
            subl.save_preferences()
            

# test
aes = sys.argv[1]
Aesthetic(aes)
