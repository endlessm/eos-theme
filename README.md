# eos-theme
Gtk, window, and icon themes for eos-shell

To build/install from this repo:
sudo apt-get install librsvg2-dev
cd ~/checkout/eos-theme
./autogen.sh --datadir=/usr/share
make
sudo make install

After installing, you will need to log out and back in
for the icon directory to be indexed.

If running eos-shell via JHBuild, you will also need the following
to install the settings properly (in addition to the above,
which is needed to install the icons):
./autogen.sh --datadir=/home/<username>/gnome/install/share
make
sudo make install

Note that any per-user settings configured with "gsettings set"
will override the system settings in the schema file that is installed.
Use "gsettings remove" for each field to restore the default
and enable use of the settings schema.
