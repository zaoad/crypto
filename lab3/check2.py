#!/usr/bin/python

# -*- coding: utf-8 -*-

blob = """
*binary blob #2 generated by hashclash, see the file by link*
"""
from hashlib import sha256
if sha256(blob).hexdigest() == '*sha256 hash of blob #1*':
	print "I come in peace."
elif sha256(blob).hexdigest() == '*sha256 hash of blob #2*':
	print "Prepare to be destroyed!"
else:
	print "Fail"
