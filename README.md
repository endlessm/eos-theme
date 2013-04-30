# eos-theme
Gtk, window, and icon themes for eos-shell

To build/install from this repo:
```
sudo apt-get install librsvg2-dev
cd ~/checkout/eos-theme
./autogen.sh --datadir=/usr/share --sysconfdir=/etc
make
sudo make install
```

Or, if running eos-shell via JHBuild:
```
jhbuild shell
./autogen.sh --prefix=$HOME/gnome/install
make
make install
```

Note that any per-user settings configured with "gsettings set"
will override the system settings in the schema file that is installed.
Use "gsettings remove" for each field to restore the default
and enable use of the settings schema.
