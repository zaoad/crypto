#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
\00\00\00\00\00\00\00\00\00\00\00>\949\BF\85"5\D4\A8,!\E5\F4\99v
HN<~MN|~k\8A1\F5\AA\DB\EF\C9JC'v\CB%\DC\D1\EF\A0\FF\E1,j\9D\B4\B4\C2YB\D8Izʜ?\A9FO\B03\81c\C0\AE\9D\A9\A3ʇ4\A1RF\AA\F2\FA|\E7\DFG[
\CB\C1!n\B0-\94\8Bi\A4\EB8\D0f8\A5\8BhU&\F5\EA\\E5@\A4\90xL
"""
blob=blob.encode("hex")
if(blob[112]=='6'):
	print('I come in peace.')
else:
	print('Prepare to be destroyed!')
