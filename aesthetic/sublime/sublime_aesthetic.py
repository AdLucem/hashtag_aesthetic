"""To err is human; to edit, sublime."""

import os
import json

class SublimeAesthetic:

    def __init__(self, data):

        self.theme = data["sublime_theme"]
        self.color_scheme = data["sublime_color_scheme"]
        self.custom_pairs = data["sublime_custom_pairs"]

        home = os.getenv("HOME")
        path = "/.config/sublime-text-3/Packages/User/Preferences.sublime-settings"
        uri = home + path
        with open(uri, "r") as f:
            self.pref = json.load(f)
            
    def change_theme(self):

        theme = self.theme
        self.pref["theme"] = theme

    def change_color_scheme(self):

        cs = self.color_scheme
        self.pref["color_scheme"] = cs

    def add_custom_pairs(self):

        pairs = self.custom_pairs
        
        for key in pairs:
            self.pref[key] = pairs[key]

    def save_preferences(self):

        home = os.getenv("HOME")
        path = "/.config/sublime-text-3/Packages/User/Preferences.sublime-settings"
        uri = home + path
        with open(uri, "w") as f:
            json.dump(self.pref, f)

