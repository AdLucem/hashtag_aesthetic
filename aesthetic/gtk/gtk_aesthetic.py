"""Beauty is in the eye of the coffee holder"""

from subprocess import call


class GTKAesthetic:

    def __init__(self, data):

        self.wallpaper = data["wallpaper"]
        self.theme = data["theme"]
        self.shell_theme = data["shell_theme"]
        self.icon_theme = data["icon_theme"]

    def change_wallpaper(self):

        wpaper_uri = "file://" + self.wallpaper

        call(["gsettings", "set",
              "org.gnome.desktop.background",
              "picture-uri", self.wallpaper])

    def change_theme(self):

        call(["gsettings", "set",
              "org.gnome.desktop.interface",
              "gtk-theme", self.theme])

    def change_shell_theme(self):

        call(["gsettings", "set",
              "org.gnome.shell.extensions.user-theme",
              "name", self.shell_theme])

    def change_icon_theme(self):

        call(["gsettings", "set",
              "org.gnome.desktop.interface",
              "icon-theme", self.icon_theme])


# test
# data = {
#     "wallpaper": "/home/ciel/Pictures/dark_building_lake.jpg",
#     "theme": "Ultimate-Dark-(Cpt)-Blue",
#     "shell_theme": "Arc-Dark",
#     "icon_theme": "Ubuntu-mono-dark"
# }

# aes = GTKAesthetic(data)
# aes.change_wallpaper()
# aes.change_theme()
# aes.change_icon_theme()
# aes.change_shell_theme()
