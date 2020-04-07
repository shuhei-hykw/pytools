#!/usr/bin/env python3

#_______________________________________________________________________________
a4size = [210.0, 297.0]
scale = 1.0
target = ''
line_width = 0.4
text_font = 'Times-Roman'
text_size = 8
wdaq = 50
hdaq = 10
wmtx = 35
hmtx = 15

#______________________________________________________________________________
def set_scale(scale_factor):
  ''' set scale factor '''
  global scale
  scale = scale_factor

#______________________________________________________________________________
def set_target(target_name):
  ''' set target '''
  global target
  target = target_name

#______________________________________________________________________________
def set_text_size(size):
  ''' set text size '''
  global text_size
  text_size = size
