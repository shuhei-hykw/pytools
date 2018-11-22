#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
from settings import a4size, line_width
import settings

#_______________________________________________________________________________
def draw():
  scale = 0.5
  settings.set_scale(scale)
  xoffset = -40
  width = 160*scale
  height = 75*scale
  t1 = 11.5*4*scale
  t2 = 90*scale
  pmt = [2.6*25.4*scale, 60*scale]
  '''front view'''
  db.draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2], width, height, line_width, 0.8)
  db.draw_square([(a4size[0]-width)/2+4+xoffset, (a4size[1])/2-pmt[1]], pmt[0], pmt[1])
  db.draw_square([(a4size[0]-width)/2-4+xoffset+width, (a4size[1])/2-pmt[1]], -pmt[0], pmt[1])
  db.draw_line_with_scale([(a4size[0]-width)/2+xoffset, a4size[1]/2+height+5], width, 5)
  db.draw_line_with_scale([(a4size[0]-width)/2-5+xoffset, a4size[1]/2], -5, height, True)
  print('{} {} moveto'.format((a4size[0]-width+pmt[0])/2+4+xoffset, a4size[1]/2+1))
  print('(Silica aerogel) dup stringwidth pop 2 div 0 exch sub 0 rmoveto show')
  print('{} {} moveto'.format((a4size[0]-width+pmt[0])/2+4+xoffset, a4size[1]/2-pmt[1]+1))
  print('(PMT R6683) dup stringwidth pop 2 div 0 exch sub 0 rmoveto show')
  # '''top view'''
  # db.draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2], width, t2, line_width, 1.0)
  # for i in range(4):
  #   db.draw_square([(a4size[0]-width)/2+xoffset, a4size[1]/2+i*t1/4], width, 11.5*scale, line_width, 0.8)
  # db.draw_circle([(a4size[0]-width)/2+xoffset+20, (a4size[1]+t2)/2], pmt[0]/2, 0.1, -1)
  # db.draw_circle([(a4size[0]-width)/2+xoffset-20+width, (a4size[1]+t2)/2], pmt[0]/2, 0.1, -1)
  xoffset += 90
  '''side view'''
  db.draw_square([(a4size[0]-pmt[0])/2+xoffset, a4size[1]/2], pmt[0], -pmt[1], line_width, 1.0)
  for i in range(4):
    db.draw_square([(a4size[0]-t2)/2+i*t1/4+xoffset, a4size[1]/2], 11.5*scale, height, line_width, 0.8)
  db.draw_line_with_scale([(a4size[0]-t2)/2+xoffset, a4size[1]/2+height+5], t1, 5)
  db.draw_line_with_scale([(a4size[0]-t2)/2+xoffset, a4size[1]/2-5], t2, -5)
  # db.draw_line_with_scale([(a4size[0]-t2)/2-5+xoffset, a4size[1]/2], -5, height, True)
  print('newpath {} {} moveto'.format((a4size[0]+t2)/2+xoffset, a4size[1]/2))
  print('{} {} rlineto'.format(-t2, 0))
  print('{} {} rlineto'.format(0, height))
  print('{} {} rlineto closepath stroke'.format(t1, 0))
  print('{} {} moveto'.format(a4size[0]/2-22+xoffset, a4size[1]/2+(height-pmt[1])/2))
  print('(Upstream) dup stringwidth pop 0 exch -2 div 0 exch rmoveto')
  print('(Upstream) dup stringwidth pop -2 div 0 rmoveto 90 rotate show -90 rotate')
  print('{} {} moveto'.format(a4size[0]/2+45+xoffset, a4size[1]/2+(height-pmt[1])/2))
  print('(Downstream) dup stringwidth pop 0 exch -2 div 0 exch rmoveto')
  print('(Downstream) dup stringwidth pop -2 div 0 rmoveto 90 rotate show -90 rotate')
  print('{} {} moveto'.format(a4size[0]/2-40+xoffset, a4size[1]/2+50))
  # print('(width = {}) dup stringwidth pop 2 div 0 exch sub 0 rmoveto show'
  #       .format(int(width/scale) if width/scale - int(width/scale) == 0 else width/scale))
  # print('{} {} moveto'.format((a4size[0])/2+xoffset, a4size[1]/2-pmt[1]+1))
  # print('(PMT) dup stringwidth pop 2 div 0 exch sub 0 rmoveto show')
  return
