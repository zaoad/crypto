#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           {�.�g��I��h0�uE���>�>��@���2�������QD���`b�EAGR�VC}�������{O��iԪm�*�w��\4������\���XY2�@�\�g����4�[�����Ī=�G{�1��"""
from hashlib import sha256
print sha256(blob).hexdigest()
blob=blob.encode("hex")
print(blob)
