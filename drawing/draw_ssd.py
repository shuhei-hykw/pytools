#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import draw_basic as db
import settings

#_______________________________________________________________________________
def draw():
  unit = 1e0
  scale = 0.036*unit
  settings.set_scale(scale)
  width = 10*345*scale
  #height = 10*350*scale
  height = 1000*scale
  sensor = {}
  sensor['thickness'] = 320*scale/unit
  sensor['spacing'] = 500*scale/unit
  space = sensor['spacing'] - sensor['thickness']
  thin_gel = 100*scale/unit
  thin_base = 180*scale/unit
  thin_full = thin_gel * 2 + thin_base
  zigzag = 2
  xstart = 10
  ystart = 40
  lw = 0.4
  lw2 = 0.1
  fc = 0.9
  ''' SSD1 '''
  x = xstart
  y = ystart
  label = ['Y', 'X', 'Y\'', 'X\'']
  for i in range(4):
    db.draw_square([x, y], sensor['thickness'], height, lw, fc)
    db.draw_square([x-1, y-1], sensor['thickness']+2, height/4, 0, 1)
    db.draw_text([x+sensor['thickness']/2, y+3], label[i])
    db.draw_line_with_scale([x, y+height], sensor['thickness'], -10)
    if i < 3:
      db.draw_line_with_scale([x+sensor['thickness']/2, y+height],
                              sensor['spacing'], 10)
      # db.draw_line_with_scale([x+sensor['thickness'], y+height],
      #                         space, 10)
    x += sensor['spacing']
  db.draw_text([(xstart+x-space)/2, y-5], 'SSD1')
  db.draw_arrow([xstart-5, y+height/2], x-xstart-space+10, 0, 2)
  db.draw_text([x+2, y+height/2+3], 'Beam')
  ''' SSD2 '''
  xstart = x + 30
  x = xstart
  label = ['X', 'Y', 'X\'', 'Y\'']
  for i in range(4):
    db.draw_square([x, y], sensor['thickness'], height, lw, fc)
    db.draw_square([x-1, y-1], sensor['thickness']+2, height/4, 0, 1)
    db.draw_text([x+sensor['thickness']/2, y+3], label[i])
    db.draw_line_with_scale([x, y+height], sensor['thickness'], -10)
    if i == 1:
      db.draw_line_with_scale([x+sensor['thickness']/2, y+height],
                              2*sensor['spacing'], 10)
      x += sensor['spacing']
    elif i < 3:
      db.draw_line_with_scale([x+sensor['thickness']/2, y+height],
                              sensor['spacing'], 10)
    x += sensor['spacing']
  db.draw_text([(xstart+x-space)/2, y-5], 'SSD2')
  db.draw_arrow([xstart-5, y+height/2], x-xstart-space+10, 0, 2)
  db.draw_text([x+2, y+height/2+3], 'Beam')
  db.draw_text([x+2, y-5], '[um]')
