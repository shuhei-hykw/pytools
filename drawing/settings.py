#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#_______________________________________________________________________________
a4size = [210.0, 297.0]
scale = 1.0
target = ''
line_width = 0.4
text_font = 'Times-Roman'
text_size = 5
wdaq = 50
hdaq = 10
wmtx = 35
hmtx = 15

#_______________________________________________________________________________
def set_scale(scale_factor):
  ''' set scale factor '''
  global scale
  scale = scale_factor

#_______________________________________________________________________________
def set_target(target_name):
  ''' set target '''
  global target
  target = target_name
