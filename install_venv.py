from venv import create
from subprocess import run

create("venv", with_pip=True)

run(["venv/Scripts/pip.exe", "install", "-r", "requirements.txt"])
