# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess


def running(program):
    p = subprocess.Popen(['tasklist.exe'], bufsize=512, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    data = p.stdout.read()
    if program in data:
        return True
    else:
        return False


def run():
    print("main: Booting Mosquitto...")
    program = "Mosquitto\Mosquitto.exe -c Mosquitto\Mosquitto.conf".split()
    subprocess.Popen(program, bufsize=512)
    print("main: Mosquitto booted.")


def close(program):
    print("main: Shutting down Mosquitto...")
    os.system("taskkill /f /im %s" % program)
    print("main: Mosquitto Shutdown.")