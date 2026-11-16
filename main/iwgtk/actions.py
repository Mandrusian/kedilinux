#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

def setup():
    options = [
        "--buildtype=release",
    ]
    mesontools.configure(" ".join(options))

def build():
    mesontools.build()

def install():
    mesontools.install()
    pisitools.removeDir("/usr/lib")
    pisitools.domove("/etc/xdg/autostart/iwgtk-indicator.desktop", "/etc/autostart")
    pisitools.removeDir("/etc/xdg")
    pisitools.dodoc("README.md", "COPYING", "CHANGELOG")