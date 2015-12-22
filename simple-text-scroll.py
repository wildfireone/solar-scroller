#!/usr/bin/env python

import scrollphat
import sys
import time
import urllib2

reading = ""
target_url = """http://pvoutput.org/service/r2/getstatus.jsp?sid=41079&key=333e82f10971475dc09a0e88ee4a78eaf13f4a66"""
for line in urllib2.urlopen(target_url):
    reading = line
reading = reading.split(",") 
output = "{:,} Kwh".format(float(reading[2]))
scrollphat.write_string("   ")

while True:
    scrollphat.scroll()
    time.sleep(0.1)
