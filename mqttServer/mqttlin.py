# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import subprocess

__author__ = "naruhodo-ryuichi"


def close(programa):
    print("main: Shutting down Mosquitto...")
    os.system("killall " + programa)
    print("main: Mosquitto Shutdown.")


def running(program):
    p = subprocess.Popen(['ps', 'ax'], bufsize=512, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    datos = p.stdout.read()
    if program in datos:
        return True
    else:
        return False


def run(program):
    print("main: Booting Mosquitto...")
    subprocess.Popen([program], bufsize=512, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print("main: Mosquitto booted.")