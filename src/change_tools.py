
from subprocess import call


def change_wallpaper_to(filelink):

    call(["gsettings",
          "set", "org.gnome.desktop.background",
          "picture-uri", filelink])


def change_theme_to(theme):

    call(["gsettings",
          "set", "org.gnome.desktop.interface",
          "gtk-theme", theme])
