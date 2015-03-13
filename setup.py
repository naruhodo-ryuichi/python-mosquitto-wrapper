# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from distutils.core import setup

__author__ = 'naruhodo-ryuichi'

setup(
    name='%s',
    version='0.1',
    packages=['mqttServer', 'mqttClients'],
    url='http://github.com/naruhodo-ryuichi/python-mosquitto-wrapper',
    license='GNU Affero General Public License',
    author='naruhodo-ryuichi',
    author_email='naruhodo-ryuichi@users.noreply.github.com',
    description='A simple wrapper for managing Mosquitto MQTT server/clients with python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ]
)
