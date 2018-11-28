#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
from settings import a4size, line_width
import settings

#_______________________________________________________________________________
def draw():
  scale = 0.4
  settings.set_scale(scale)
  xoffset = -30
  cframe = 0.6
  hframe = [176*scale,   8*scale, 78*scale]
  vframe = [  8*scale, 123*scale, 78*scale]
  caerogel = 0.8
  aerogel = [116*scale, 107*scale, 31*scale]
  yspace = (vframe[1]-aerogel[1])/2
  window = [225*scale, 162*scale]
  pmt = [2.5*25.4*scale, 60*scale]
  pmt_dist = 78*scale
  mirror = 40*scale
  height = hframe[1]*2 + vframe[1]
  '''front view'''
  x = a4size[0]/2+xoffset
  y = a4size[1]/2
  for i in range(2):
    for j in range(2):
      db.draw_square([x-pmt[0]/2+(2*(i%2)-1)*pmt_dist/2,
                      y-pmt[1]+j*(pmt[1]+height)],
                     pmt[0], pmt[1], line_width)
  db.draw_square([x-hframe[0]/2, y], hframe[0], hframe[1],
                 line_width, fill_color=cframe)
  db.draw_square([x-hframe[0]/2, y+hframe[1]+vframe[1]],
                 hframe[0], hframe[1], line_width, fill_color=cframe)
  db.draw_square([x-hframe[0]/2, y+hframe[1]], vframe[0], vframe[1],
                 line_width, fill_color=cframe)
  db.draw_square([x+hframe[0]/2, y+hframe[1]], -vframe[0], vframe[1],
                 line_width, fill_color=cframe)
  db.draw_square([x-aerogel[0]/2, y+hframe[1]+yspace],
                 aerogel[0], aerogel[1], line_width, fill_color=caerogel)
  # db.draw_line_with_scale([x-hframe[0]/2, y+height+pmt[1]],
  #                         hframe[0], 16)
  db.draw_line_with_scale([x-hframe[0]/2+vframe[0],
                           y+height+pmt[1]],
                          hframe[0]-vframe[0]*2, 6)
  # db.draw_line_with_scale([x-hframe[0]/2, y],
  #                         -16, height, True)
  db.draw_line_with_scale([x-hframe[0]/2, y+hframe[1]],
                          -6, vframe[1], True)
  db.draw_line_with_scale([x-aerogel[0]/2, y+hframe[1]+(vframe[1]+aerogel[1])/2],
                          aerogel[0], -10)
  db.draw_line_with_scale([x-aerogel[0]/2, y+hframe[1]+yspace],
                          10, aerogel[1], True)
  db.draw_arrow([(a4size[0]-pmt[0])/2+xoffset, a4size[1]/2-pmt[1]+2], 4, -4, 3)
  db.draw_arrow([(a4size[0]+pmt[0])/2+xoffset, a4size[1]/2-pmt[1]+2], -4, -4, 3)
  db.draw_text([x, y-pmt[1]-6], 'PMT R6682')
  db.draw_text([x+aerogel[0]*0.2-12, y+hframe[1]+vframe[1]/2-1.5], 'Beam')
  db.draw_beam_mark([x+aerogel[0]*0.2, y+hframe[1]+vframe[1]/2], 5)
  x += 90
  '''side view'''
  db.draw_square([x-hframe[2]/2, y], hframe[2], hframe[1],
                 line_width, fill_color=cframe)
  db.draw_square([x-hframe[2]/2, y+hframe[1]+vframe[1]],
                 hframe[2], hframe[1], line_width, fill_color=cframe)
  db.draw_square([x-pmt[0]/2, y-pmt[1]], pmt[0], pmt[1], line_width)
  db.draw_square([x-pmt[0]/2, y+height], pmt[0], pmt[1], line_width)
  db.draw_square([x-hframe[2]/2, y+hframe[1]],
                 hframe[2], vframe[1], line_width)
  db.draw_square([x-hframe[2]/2, y+hframe[1]+yspace],
                 aerogel[2], aerogel[1], line_width, caerogel)
  db.draw_polygon([x+hframe[2]/2, y+hframe[1]],
                  [[-mirror, vframe[1]/2],
                   [mirror, vframe[1]/2]], line_width)
  db.draw_line_with_scale([x-hframe[2]/2, y+height+pmt[1]],
                          hframe[2], 6)
  db.draw_line_with_scale([x-hframe[2]/2,
                           y+hframe[1]+(vframe[1]+aerogel[1])/2],
                          aerogel[2], -10)
  db.draw_arrow([x-hframe[2]/2+aerogel[2]-1,
                 y+hframe[1]+yspace+aerogel[1]-1],
                hframe[2]-aerogel[2]+4, 3, 3)
  db.draw_text([x+hframe[2]/2+28, y+height*0.9],
               'Silica aerogel (n=1.12)')
  db.draw_arrow([x+hframe[2]/2-2.5,
                 y+height*0.1+1.5], 6, 0, 3)
  db.draw_text([x+hframe[2]/2+18, y+height*0.1], 'Teflon mirror')
  db.draw_arrow([x-hframe[2]/2-5, y+height/2-6], hframe[2]+10, 0, 2)
  db.draw_text([x+hframe[2]/2+8, y+height/2-3], 'Beam')
  db.draw_text([x+hframe[2]/2+30, y-pmt[1]-6], '[mm]')
