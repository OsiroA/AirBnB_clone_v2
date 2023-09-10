#!/usr/bin/python3
"""
this fabric script uses the previous one created to distribute an archive
to teh web-servers, using the function do_deploy
"""
from time import strftime
from fabric.api import local
from os import path
from fabric.api import run, env, put
env.hosts = ['54.237.88.25', '54.90.40.27']
env.user = "ubuntu"


def do_pack():
    """this generates a .tgz archive"""
    currentTime = strftime("%Y%M%d%H%M%S")

    local("mkdir -p versions")
    archivedFilePath = "versions/web_static_{}.tgz".format(currentTime)
    local("tar -cvzf {} web_static/".format(archivedFilePath))
    return archivedFilePath


def do_deploy(archive_path):
    """This distributes a .tgz archive through web servers"""
    if path.exists(archive_path):
        archives = archive_path.split('/')[1]
        archived_path = "/tmp/{}".format(archives)
        a_folder = archives.split('.')[0]
        folderPath = "/data/web_static/releases/{}/".format(a_folder)
        put(archive_path, archived_path)
        run("sudo mkdir -p {}".format(folderPath))
        run("sudo tar -xzf {} -C {}".format(archived_path, folderPath))
        run("sudo rm {}".format(archived_path))
        run("sudo mv -f {}web_static/* {}".format(folderPath, folderPath))
        run("sudo rm -rf {}web_static".format(folderPath))
        run("sudo rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folderPath))
        return True
    else:
        return False


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success
