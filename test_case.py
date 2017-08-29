#!/usr/bin/python
# -*- coding:utf-8 -*-

from arabic_processing_cog.tokenization import ArabicTokenizer as at
from arabic_processing_cog.stemming import Light10stemmer as l10

if __name__ == "__main__":
    for token in at.tokenize("وزير انا عايز قلش في كل مكان عايز الناس كلها تقلش دا انا ابويا مهرج عليا مزعلجش ههرج مخدرات"):
        print(token)
        print(l10.stem_token(token))

