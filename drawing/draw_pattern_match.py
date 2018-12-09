#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import draw_basic as db
import settings

version = 2

#_______________________________________________________________________________
def draw():
  scale = 1.0
  settings.set_scale(scale)
  xstart = 10
  ystart = 100
  x = xstart
  y = ystart
  w = 50*scale
  h = 50*scale
  ''' SSD1 '''
  db.draw_square([x, y], w, h)
  ''' Emulsion '''
  x += w*2
  db.draw_square([x, y], w, h)
