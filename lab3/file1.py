#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           {�.�g��I��h0�uE����>��@���2�������QD���`b��AGR�VC}����S��{O��iԪm�*�w��\4��c���\���XY2�@�\�g����4Z\�����Ī=�G{h1��"""
from hashlib import sha256
print sha256(blob).hexdigest()
blob=blob.encode("hex")
print(blob)
