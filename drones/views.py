# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from PIL import Image
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
from django.http import HttpResponse

import cv2
import numpy as np

import drones
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
    ret, img = drones.cap.read()
    ret,img_webp = cv2.imencode(".webp", img)
    try:
##        with open(os.readlink("/home/pi/drone_server/latest.webp"), "rb") as f:
        
        return HttpResponse(img_webp.tobytes(), content_type="image/webp")
    except IOError:
        print "latest.webp not found"
        red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
        response = HttpResponse(content_type="image/webp")
        red.save(response, "JPEG")
        return response






def create_latest(request):
    # initialising video capture object: camera
##    cap = cv2.VideoCapture(0)
##    w = 800
##    h = 448
##    cap.set(3,w);
##    cap.set(4,h);
    
    # capture frame and save as jpg
    ret, img = cap.read()
    new_filename = '/home/pi/images/img_{}.webp'.format(time.asctime()).replace(":",".").replace(" ","-")
    cv2.imwrite(new_filename,img)
    os.system("ln -sf " + new_filename + " /home/pi/drone_server/latest.webp")
    return HttpResponse("success")
