#!/bin/bash
# -*- coding: UTF8 -*-
cat /etc/shadow
ps -aux
gsutil ls
python yolo.py
gsutil ls
