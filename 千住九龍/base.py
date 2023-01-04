#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os
from bottle import route, run, template, view, request, response, redirect, static_file
from datetime import datetime
from NewFolder2 import routesTopMain
from NewFolder2 import routesAdmin

import logging
from bottle import Bottle, debug
bottle = Bottle()
debug(True)

import warnings
warnings.filterwarnings('ignore')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'NewFolder2/NewFolder1/static').replace('\\', '/')
STATIC_ROOT_BATTLELOG = os.path.join(PROJECT_ROOT, 'NewFolder2/NewFolder1/battleLog').replace('\\', '/')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=STATIC_ROOT)

@route('/battleLog/<filepath:path>')
def server_static_battleLog(filepath):
    return static_file(filepath, root=STATIC_ROOT_BATTLELOG)

# for production (Linux)
run(server='cgi')