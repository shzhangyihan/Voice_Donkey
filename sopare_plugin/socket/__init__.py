#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 - 2017 Martin Kauss (yo@bishoph.org)

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

# Plugin for sending analysis to socket servers
from socket import socket
import sys

#HOST = gethostbyname('localhost')
HOST = '192.168.8.127'
PORT = 8888
print HOST
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
print "HELLOHELLOHELLOHELLO"

def run(readable_results, data, rawbuf):
    for r in readable_results:
        print r
        s.send(r)
