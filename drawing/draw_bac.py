#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
from settings import a4size, line_width
import settings

#_______________________________________________________________________________
def draw(top_view=False):
  scale = 0.5
  settings.set_scale(scale)
  xoffset = -30
  yoffset = -30
  width = 180*scale
  height = 80*scale
  window = [170*scale, 70*scale]
  t1 = 11.5*4*scale
  t2 = 90*scale
  pmt = [3.0*25.4*scale, 60*scale]
  pmt_dist = 90*scale
  pmt_offset = (width - pmt_dist - pmt[0])/2
  '''front view'''
  x = a4size[0]/2 + xoffset
  y = a4size[1]/2 + yoffset
  db.draw_square([x-width/2+pmt_offset, y-pmt[1]],
                 pmt[0], pmt[1], line_width)
  db.draw_square([x+width/2-pmt_offset, y-pmt[1]],
                 -pmt[0], pmt[1], line_width)
  db.draw_square([x-width/2, y], width, height, line_width)
  db.draw_square([x-window[0]/2, y+(height-window[1])/2],
                 window[0], window[1], line_width, 0.8)
  db.draw_line_with_scale([x-width/2, y+height], width, 16)
  db.draw_line_with_scale([x-window[0]/2, y+height], window[0], 5)
  db.draw_line_with_scale([x-width/2, y], -16, height, True)
  db.draw_line_with_scale([x-width/2, y+(height-window[1])/2],
                          -5, window[1], True)
  db.draw_arrow([x-pmt[0]/2, y-pmt[1]+2], 4, -4, 3)
  db.draw_arrow([x+pmt[0]/2, y-pmt[1]+2], -4, -4, 3)
  db.draw_text([x, y-pmt[1]-6], 'PMT R6683')
  db.draw_text([x-12, y+height/2-1.5], 'Beam')
  db.draw_beam_mark([x, y+height/2], 5)
  '''side view'''
  x += 200*scale
  db.draw_polygon([x+t2/2, y], [[-t2, 0], [0, height], [t1, 0]],
                  line_width)
  db.draw_square([x-pmt[0]/2, y], pmt[0], -pmt[1], line_width, 1.0)
  for i in range(4):
    db.draw_square([x-t2/2+i*t1/4, y], 11.5*scale, height, line_width, 0.8)
  db.draw_line_with_scale([x-t2/2, y+height], t1, 5)
  db.draw_line_with_scale([x-t2/2, y], t2, -10)
  db.draw_arrow([x-2, y+height-6], 6, 4, 3)
  db.draw_text([x+t1/2+17, y+height-1], 'Silica aerogel (n=1.03)')
  db.draw_arrow([x+t1/2+6.5, y+8], 3, 0, 3)
  db.draw_text([x+t1/2+24, y+6.5], 'Teflon mirror')
  db.draw_arrow([x-t2/2-5, y+height/2], t2+10, 0, 2)
  db.draw_text([x+t2/2, y+height/2+2], 'Beam')
  db.draw_text([x+t2/2+15, y-pmt[1]-6], '[mm]')
  '''top view'''
  if not top_view:
    return
  xoffset += -200*scale
  yoffset += 150*scale
  db.draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2+yoffset], width, t2, line_width)
  for i in range(4):
    db.draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2+yoffset+i*t1/4], width, t1/4, line_width, 0.8)
  db.draw_circle([(a4size[0]-width)/2+pmt_offset+xoffset+pmt[0]/2,
                  (a4size[1])/2+t2/2+yoffset], pmt[0]/2, fc=-1)
  db.draw_circle([(a4size[0]-width)/2-pmt_offset+xoffset+width-pmt[0]/2,
                  (a4size[1])/2+t2/2+yoffset], pmt[0]/2, fc=-1)
  db.draw_line_with_scale([(a4size[0]-width)/2+xoffset, a4size[1]/2+yoffset], -16, t2, True)
  db.draw_line_with_scale([(a4size[0]-width)/2+xoffset, a4size[1]/2+yoffset], -5, t1, True)
