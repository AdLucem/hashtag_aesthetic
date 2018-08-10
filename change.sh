# "Life is fleeting, change is eternal"


# setting the background
if [ "$1" == 'dark' ]; then
    gsettings set org.gnome.desktop.background picture-uri 'file:///home/ciel/github/Config-Files/cl-specific-config/dark_building_lake.jpg'
else
                gsettings set org.gnome.desktop.background picture-uri 'file:///home/ciel/github/Config-Files/cl-specific-config/night_mountain_sea_moon.jpg'
fi

# setting the theme
gsettings set org.gnome.desktop.interface gtk-theme "Arc-Dark"

# setting dark mode to ON
cd ~
touch ~/.config/gtk-3.0/settings.ini
echo [Settings] > ~/.config/gtk-3.0/settings.ini
echo gtk-application-prefer-dark-theme=1 >> ~/.config/gtk-3.0/settings.ini
