#!/usr/bin/env python

## "author" = "Kapil Gupta"
## "copyright" = "Copyright 2016, TheMallCloud"
## "credits" = ["Kapil Gupta"]
## "license" = "GPL"
## "version" = "1.0.1"
## "maintainer" = "Kapil Gupta"
## "email" = "kpgupta98@gmail.com"
## "status" = "Production"


from __future__ import absolute_import
from __future__ import print_function


import json

import sys
sys.path.append('..')

import os.path
import models_pb2 as models


path_to_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "server", "config.json")
path_to_book = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "features", "parameters_book.prototxt")

with open(path_to_json) as conf_file:
	conf = json.load(conf_file)

def CheckTemplatesNeeded(templates) :
  pass

def CreateTemplates(templates) :
	CheckTemplatesNeeded(templates)


parameters_book = models.Models()

try:
	with open(path_to_book, 'rb') as file:
		parameters_book.ParseFromString(file.read())
except IOError:
	print('[!] Parameters Book not present, creating new book')

CreateTemplates(parameters_book.templates.add())

with open(path_to_book, 'wb') as file:
	file.write(parameters_book.SerializeToString())
