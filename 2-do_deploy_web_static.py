#!/usr/bin/python3
from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['54.242.46.167', '54.234.143.129']

#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['localhost']


def do_pack():
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1].split(".")[0]

        # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
        run("mkdir -p /data/web_static/releases/{}/".format(filename))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(filename, filename))

        # Delete the archive from the web server
        run("rm /tmp/{}.tgz".format(filename))

        # Move the contents of the web_static folder up one level
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(filename, filename))

        # Delete the web_static folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(filename))
        return True

    except:
        return False
