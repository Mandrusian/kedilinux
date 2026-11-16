if [ "$(id -u)" = 0 ] && [ "$(tty)" = /dev/tty1 ] && [ -z "$DISPLAY" ]; then
    startx /usr/bin/kedi-installer-session
fi
