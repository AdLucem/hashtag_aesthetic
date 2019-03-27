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
from shell_aesthetic import ShellAesthetic
from gtk_aesthetic import GTKAesthetic


class AestheticMissingError(Exception):
    """Define a custom error for when the Aesthetic
    file is not found"""
    pass


def fetch(filename):

    try:
        with open(filename, "r+") as f:
            data = json.loads(f)
    except IOError:
        data = {}

    return data


class Aesthetic:
    """
        Nothing's perfect, the world's not perfect.
        But it's there for us, trying the best it can;
        that's what makes it so damn beautiful.
    """

    def __init__(filename):

        try:
            data = fetch(filename)
            if data == {}:
                raise AestheticMissingError

            gtk = GTKAesthetic(data)
            terminal = ShellAesthetic(data)
            emacs = EmacsAesthetic(data)
            subl = SublimeAesthetic(data)

        except AestheticMissingError:
            print("Error: Aesthetic file not found")


