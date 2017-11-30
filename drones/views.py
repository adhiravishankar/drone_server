# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import Image
import dircache
import random

import os

from shutil import copyfile

import time

from datetime import datetime
from django.http import HttpResponse
# Create your views here.


def index(request):
    try:
        with open("images/latest.jpg", "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")
        return response


def create_latest(request):
    dir = '/home/adhi/Downloads/photos/TolerPresley_files'
    filename = random.choice(dircache.listdir(dir))
    path = os.path.join(dir, filename)
    new_file = 'images/timestamped/' + datetime.now().isoformat().__str__() + ".jpg"
    copyfile(path, new_file)
    os.system("ln -f " + new_file + " /home/adhi/PycharmProjects/drone_server/images/latest.jpg")
    return HttpResponse("success")
