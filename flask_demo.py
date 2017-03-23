#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-23 17:30:48
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
	return 'hello flask!'  
  
if __name__ == '__main__':
	app.run() 