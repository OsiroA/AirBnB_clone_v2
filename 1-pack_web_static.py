#!/usr/bin/python3
"""
This is a fabric script that generates a .tgz archive
from the contents of the 'web-static' folder of the AirBnB clone repo
using the function do-pack
"""
from time import strftime
from fabric.api import local


def do_pack():
    """this generates a .tgz archive"""
    currentTime = strftime("%Y%M%d%H%M%S")

    local("mkdir -p versions")
    archivedFilePath = "versions/web_static_{}.tgz".format(currentTime)
    local("tar -cvzf {} web_static/".format(archivedFilePath))
    return archivedFilePath
