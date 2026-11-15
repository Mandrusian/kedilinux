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
    pisitools.insinto("/etc", "etc/calamares")
    pisitools.insinto("/etc", "etc/sudoers.d")
    pisitools.insinto("/etc", "etc/polkit-1")
    pisitools.insinto("/usr/share/applications", "usr/share/applications/kedi-install.desktop")