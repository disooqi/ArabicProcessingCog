#!/usr/bin/python
# -*- coding:utf-8 -*-
from arabic_processing_cog.tokenization import ArabicTokenizer as at

if __name__ == "__main__":
    for token in at.tokenize("بسم الله الرحن الرحيم"):
        print token
