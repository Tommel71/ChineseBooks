#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from __future__ import unicode_literals

from argparse import ArgumentParser

from PETRUS.g2p.g2p import G2PTranscriber

import os
import codecs
def get_phonetics(word):

    if word == " ": return " "

    try:

        # Get input word
        word = word.strip().lower()
        # Initialize g2p transcriber
        g2p = G2PTranscriber(word, algorithm="silva")
        transcript = g2p.transcriber()
        # Write file
    except Exception as e:
        transcript = ""

    return transcript
