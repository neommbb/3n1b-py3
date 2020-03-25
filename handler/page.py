#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2013 3n1b.com

import uuid
import hashlib
import image
from io import StringIO     #  # in py3,StringIO is contained in io
import time
import json
import re
import urllib.request
import urllib.error
import tornado.web
import lib.jsonp

from base64 import *
from lib.variables import *

class AboutHandler(urllib.request.BaseHandler):      # before is "baseHandler",now is"urllib.request.BaseHandler"
    def get(self, template_variables = {}):
    	template_variables["wallpaper"] = self.get_wallpaper()
        self.render("page/about.html", **template_variables)
