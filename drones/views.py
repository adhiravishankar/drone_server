# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Image
import dircache
import json
import random

import os
import urllib

from shutil import copyfile

import time

from datetime import datetime
from django.http import HttpResponse, StreamingHttpResponse
from django.core.cache import cache
# Create your views here.


def index(request):
    url = "http://localhost:8000/api/v1/shape/?format=json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    if 'detail' in data:
        return HttpResponse(cache.get('latest'), content_type="image/webp")
    else:
        down = data['down']
        up = data['up']
        up_rate = up['rate']
        down_rate = down['rate']






def create_latest(request):
    dir = '/home/adhi/Downloads/photos/eng'
    filename = random.choice(dircache.listdir(dir))
    path = os.path.join(dir, filename)
    new_file = 'images/timestamped/' + datetime.now().isoformat().__str__() + ".webp"
    os.system('cwebp -q 90 ' + path + ' -o ' + new_file)
    os.system("ln -f " + new_file + " /home/adhi/PycharmProjects/drone_server/images/latest.webp")
    cache.set('latest', open("images/latest.webp", "r").read(), None)
    return HttpResponse("success")
