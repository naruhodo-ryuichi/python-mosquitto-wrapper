# -*- coding: utf-8 -*-
"""
Created on 24/05/2012

@author: Peter
"""
import os
from threading import Thread


class mqttServer(Thread):
    """
    wrapper for Mosquitto exe for linux/windows
    """

    def __init__(self):
        Thread.__init__(self)

    def start(self):
        if os.name == "nt":
            from mqttwin import running, close, run
        elif os.name == "posix":
            from mqttlin import running, close, run
            if running("Mosquitto"):
                close("Mosquitto")
            run()


if __name__ == '__main__':
    t = mqttServer()
    t.start()
