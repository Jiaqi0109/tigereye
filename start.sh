#!/bin/bash


cd /home/jiaqi/Documents/stageIII/tigereye
/home/jiaqi/Documents/stageIII/tigereye/env/bin/gunicorn -w4 -D wsgi
ps aux | grep gunicorn | grep tigereye | grep -v grep
