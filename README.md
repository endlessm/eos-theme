# eos-theme
Gtk, window, and icon themes for eos-shell

To build/install from this repo:
```
sudo apt-get install gnome-common librsvg2-dev libgtk-3-dev
cd ~/checkout/eos-theme
./autogen.sh --prefix=/usr --sysconfdir=/etc
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
Note that for jhbuild to show the full theme, you need to create a new
xsessions file (ex: /usr/share/xsessions/eos-session.desktop) with the
following
content:
```
[Desktop Entry]
Name=EOS
Comment=This session logs you into GNOME
Exec=jhbuild run gnome-session --session=eos-shell
Icon=
Type=Application
X-Ubuntu-Gettext-Domain=gnome-session-3.0
```

Note also that any per-user settings configured with "gsettings set"
will override the system settings in the schema file that is installed.
Use "gsettings reset" for each field to restore the default
and enable use of the settings schema.
