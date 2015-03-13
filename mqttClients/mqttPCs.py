# -*- coding: utf-8 -*-
import socket
import time
from mosquitto import Mosquitto


class Service():
    def __init__(self):
        myhost = socket.gethostname()
        hostslist = set()
        conf = {
            "mqttserver": "127.0.0.1:1883"
        }


class mqttPCs(Mosquitto):
    """
    Subscribes to a remote event dispatcher.
    Generates a sets of servers
    updates the set dynamically depending on each machine's on/off status
    """

    def __init__(self, serv):
        Mosquitto.__init__(self)
        self.serv = serv

    @staticmethod
    def on_connect(self, result):
        print("mqttpcs: connected: %d" % result)

    @staticmethod
    def on_disconnect(self):
        print("mqttpcs: disconnected")

    @staticmethod
    def on_message(self, msg):
        print("message received %s" % msg)
        remhost = msg.topic.split("/")[1]
        if msg.payload == "on":
            self.serv.hostslist.add(remhost)
        if msg.payload == "off":
            self.serv.hostslist.remove(remhost)
            # print("%s" % serv.hostslist)

    @staticmethod
    def on_publish(self, mid):
        print("mqttpcs: Published mid: %d" % mid)

    @staticmethod
    def on_subscribe(self, mid, granted_qos):
        print("mqttpcs: Subscribed: %d %s" % (mid, str(granted_qos)))

    def run(self):
        self.will_set(("pcs/%s" % self.serv.myhost), "off")
        self.connect(self.serv.conf["mqttserver"])
        print("mqttpcs: %s connecting to %s..." % (self._client_id, self._host))
        # subscribe to pcs
        self.subscribe("pcs/+")
        self.loop()
        # publish our state
        self.publish(("pcs/%s" % self.serv.mihost), "on", retain=True)
        self.loop()
        # main loop
        rc = 0
        while rc == 0:
            rc = self.loop()
            time.sleep(1)
            print("mqttpcs: " + str(self.serv.hostslist))


if __name__ == '__main__':
    serv = Service()
    t = mqttPCs(serv)
    t.start()
