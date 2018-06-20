#!/usr/bin/env python
# -*- coding: utf-8 -*-

import errno
import os
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape

"""
Compiles/renders templates

File lookup in ./src/templates folder

    $ python render_template.py <filename>
"""

env = Environment(
    extensions=['jinja2htmlcompress.HTMLCompress'],
    loader=FileSystemLoader('src/templates'),
    autoescape=select_autoescape(['html'])
)

if len(sys.argv) < 2:
    raise ValueError('No file supplied as parameter.')

filename = sys.argv[1]

if not os.path.isfile(filename):
    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT), filename)

template_name = filename.replace('src/templates/', '')

template = env.get_template(template_name)

print template.render()
