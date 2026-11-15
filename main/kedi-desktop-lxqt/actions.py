#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr/share/themes", "usr/share/themes/Kedi-dark")
    pisitools.insinto("/usr/share/lxqt/themes", "usr/share/lxqt/themes/kedi")
    pisitools.insinto("/usr/share/backgrounds", "usr/share/backgrounds/kedi")
    pisitools.insinto("/usr/share/pixmaps", "usr/share/pixmaps/kedi-menu-icon.png")
    pisitools.insinto("/usr/share/doc", "usr/share/doc/kedi-desktop-lxqt")
    pisitools.insinto("/etc/xdg", "etc/xdg/lxqt")
    pisitools.insinto("/etc/xdg", "etc/xdg/pcmanfm-qt")
    pisitools.insinto("/etc/skel", "etc/skel/.config")