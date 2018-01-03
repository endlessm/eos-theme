# /etc/profile.d/eos-icon-theme.sh
# add Endless OS icon theme Flatpak extension to XDG_DATA_DIRS

if [ "${XDG_DATA_DIRS#/run/share}" = "${XDG_DATA_DIRS}" ]; then
    if [ -e /run/share-extra/icons/EndlessOS ]; then
        XDG_DATA_DIRS="/run/share-extra/:${XDG_DATA_DIRS:-/usr/local/share/:/usr/share/}"
    fi
    if [ -e /run/share/icons/EndlessOS ]; then
        XDG_DATA_DIRS="/run/share/:${XDG_DATA_DIRS:-/usr/local/share/:/usr/share/}"
    fi
fi

export XDG_DATA_DIRS
