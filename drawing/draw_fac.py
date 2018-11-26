#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
from settings import a4size, line_width
import settings

#_______________________________________________________________________________
def draw():
  scale = 0.3
  settings.set_scale(scale)
  xoffset = -30
  width = 241*scale
  height = 165*scale
  window = [225*scale, 162*scale]
  t1 = 65*scale
  t2 = 65*scale
  pmt = [2.5*25.4*scale, 60*scale]
  pmt_dist = 75*scale
  pmt_offset = (width - pmt_dist - pmt[0])/2
  '''front view'''
  db.draw_square([a4size[0]/2+xoffset-pmt[0]/2, (a4size[1])/2-pmt[1]], pmt[0], pmt[1], line_width)
  db.draw_square([a4size[0]/2+xoffset-pmt[0]/2+pmt_dist, (a4size[1])/2-pmt[1]], pmt[0], pmt[1], line_width)
  db.draw_square([a4size[0]/2+xoffset-pmt[0]/2-pmt_dist, (a4size[1])/2-pmt[1]], pmt[0], pmt[1], line_width)
  db.draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2], width, height, line_width)
  db.draw_square([(a4size[0]-window[0])/2+xoffset, (a4size[1]+height-window[1])/2], window[0], window[1], line_width, 0.8)
  db.draw_line_with_scale([(a4size[0]-width)/2+xoffset, a4size[1]/2+height], width, 16)
  db.draw_line_with_scale([(a4size[0]-window[0])/2+xoffset, a4size[1]/2+height], window[0], 5)
  db.draw_line_with_scale([(a4size[0]-width)/2+xoffset, a4size[1]/2], -16, height, True)
  db.draw_line_with_scale([(a4size[0]-width)/2+xoffset, (a4size[1]+height-window[1])/2], -5, window[1], True)
  #db.draw_text([(a4size[0]-width+pmt[0])/2+4+xoffset, (a4size[1]+height-window[1])/2+1.5], 'Sensitive region')
  #db.draw_text([(a4size[0]-width+pmt[0])/2+4+xoffset, a4size[1]/2-pmt[1]+1], 'PMT R6683')
  db.draw_arrow([(a4size[0]-pmt[0])/2+xoffset, a4size[1]/2-pmt[1]+2], 4, -4, 3)
  db.draw_arrow([(a4size[0]+pmt[0])/2+xoffset, a4size[1]/2-pmt[1]+2], -4, -4, 3)
  db.draw_text([(a4size[0])/2+xoffset, a4size[1]/2-pmt[1]-6], 'PMT R6683')
  # '''top view'''
  # db.draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2], width, t2, line_width, 1.0)
  # for i in range(4):
  #   db.draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2+i*t1/4], width, 11.5*scale, line_width, 0.8)
  # db.draw_circle([(a4size[0]-width)/2+xoffset+20, (a4size[1]+t2)/2], pmt[0]/2, 0.1, -1)
  # db.draw_circle([(a4size[0]-width)/2+xoffset-20+width, (a4size[1]+t2)/2], pmt[0]/2, 0.1, -1)
  db.draw_text([(a4size[0])/2+xoffset-12, a4size[1]/2+height/2-1.5], 'Beam')
  db.draw_beam_mark([(a4size[0])/2+xoffset, a4size[1]/2+height/2], 5)
  xoffset += 90
  '''side view'''
  db.draw_polygon([(a4size[0]+t2)/2+xoffset, a4size[1]/2], [[-t2, 0], [0, height], [t1, 0]], line_width)
  db.draw_square([(a4size[0]-pmt[0])/2+xoffset, a4size[1]/2], pmt[0], -pmt[1], line_width, 1.0)
  for i in range(4):
    db.draw_square([(a4size[0]-t2)/2+i*11.5/4+xoffset, a4size[1]/2], 11.5*scale, height, line_width, 0.8)
  db.draw_line_with_scale([(a4size[0]-t2)/2+xoffset, a4size[1]/2+height], t1, 5)
  db.draw_line_with_scale([(a4size[0]-t2)/2+xoffset, a4size[1]/2], t2, -10)
  db.draw_arrow([(a4size[0])/2+xoffset-2, (a4size[1])/2+height-6], 6, 4, 3)
  db.draw_text([(a4size[0]+t1)/2+7+xoffset, (a4size[1])/2+height-1], 'Silica aerogel')
  db.draw_arrow([(a4size[0]-t2)/2+xoffset-5, a4size[1]/2+height/2], t2+10, 0, 2)
  db.draw_text([(a4size[0]+t2)/2+xoffset, a4size[1]/2+height/2+2], 'Beam')
  # db.draw_line_with_scale([(a4size[0]-t2)/2-5+xoffset, a4size[1]/2], -5, height, True)
