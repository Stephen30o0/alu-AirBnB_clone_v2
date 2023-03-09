#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['localhost']


def do_pack():
    """ Creates .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None
