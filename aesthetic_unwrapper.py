"""Nothing's perfect, the world's not perfect.
But it's there for us, trying the best it can;
that's what makes it so damn beautiful."""

import json
from change_tools import change_wallpaper_to,
change_theme_to


class EmacsAesthetic:
    """Emacs is like a laser guided missile.
    It only has to be slightly mis-configured
    to ruin your whole day."""

    def __init__(self, details):
        self.theme = details["theme"]
        self.transparency = details["transparency"]


class SublimeAesthetic:
    """To err is human; to edit, sublime."""

    def __init__(self, details):
        self.theme = details["theme"]
        self.color_scheme = details["color-scheme"]


class Aesthetic:
    """Beauty is in the eye of the coffee holder."""

    wallpaper_home_dir = "file:///home/kw/Pictures/Wallpapers/"

    def __init__(self, details):

        self.wallpaper = Aesthetic.wallpaper_home_dir + details["wallpaper"]
        self.theme = details["theme"]
        self.shell_theme = details["shell-theme"]
        self.is_dark = details["dark"]
        self.emacs = EmacsAesthetic(details["emacs"])
        self.sublime = SublimeAesthetic(details["sublime"])

    @staticmethod
    def apply(aesthetic):

        change_wallpaper_to(self.wallpaper)
        change_theme_to(self.theme)
        set_dark_to(self.is_dark)


class AestheticUnwrapper:
    """Visual art and writing don't exist on an aesthetic hierarchy
    that positions one above the other, because each is capable of
    things the other can't do at all. Sometimes one picture is equal
    to 30 pages of discourse, just as there are things images are
    completely incapable of communicating."""

    aesthetics_home_dir = "/home/kw/.aesthetics/"

    def __init__(self):
        pass

    @staticmethod
    def load_aesthetic_from_file(name):

        self.aesthetic_file = aesthetics_home_dir + name

        try:
            with open(self.aesthetic_file, "r+") as f:
                details = json.load(f)
        except IOError:
            print("Error: aesthetic file not found.")
            aesthetic = Aesthetic(default_details)

        aesthetic = Aesthetic(details)
        return aesthetic
