# eos-theme
Gtk, window, and icon themes for eos-shell

To build/install from this repo:
```
sudo apt-get install gnome-common librsvg2-dev libgtk-3-dev libgtk2.0-dev
cd ~/checkout/eos-theme
./autogen.sh --datadir=/usr/share --sysconfdir=/etc
make
sudo make install
```

Or, if running eos-shell via JHBuild:
```
jhbuild shell
./autogen.sh --prefix=$HOME/gnome/install (for 32-bit systems)
./autogen.sh --prefix=$HOME/gnome/install --libdir=$HOME/gnome/install/lib64 (for 64-bit systems)
make
make install
```

Note that any per-user settings configured with "gsettings set"
will override the system settings in the schema file that is installed.
Use "gsettings reset" for each field to restore the default
and enable use of the settings schema.
