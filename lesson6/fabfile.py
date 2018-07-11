from fabric.api import env, run, local, cd, sudo

import os


env.hosts = ["54.164.88.110"]
env.user = "ubuntu"
env.key_filename = ["/home/anastasiya/keyvirg.pem"]

def test():
    run("date")
    local("date")

def update():
    with cd("/home/ubuntu/LearnPython/lesson6"):
        run("git pull")
        sudo("supervisorctl restart server")
