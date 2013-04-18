# eos-theme
Gtk, window, and icon themes for eos-shell

To build/install from this repo:
sudo apt-get install librsvg2-dev
cd ~/checkout/eos-theme
./autogen.sh --datadir=/usr/share
make
sudo make install

Note that any per-user settings configured with "gsettings set"
will override the system settings in the schema file that is installed
