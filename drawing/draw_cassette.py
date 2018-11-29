#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
from settings import a4size, line_width
import settings

#_______________________________________________________________________________
def draw(top_view=False):
  scale = 0.18
  settings.set_scale(scale)
  x = a4size[0]/2 - 30
  y = a4size[1]/2
  '''
  back view
  '''
  ss = [[390*scale, 440*scale, 0*scale, 1], #x, y, yoffset, color
        [390*scale, 395*scale, 0*scale, 1],
        [376.2*scale, 381.2*scale, 9.9*scale, 1],
        [358.2*scale, 363.2*scale, 18.9*scale, 1],
        [346*scale, 351*scale, 25*scale, 0.8],
  ]
  for i, s in enumerate(ss):
    db.draw_square([x-s[0]/2, y+s[2]], s[0], s[1],
                   line_width=line_width, fill_color=s[3])
    if i == 0:
      db.draw_line_with_scale([x-s[0]/2, y+s[1]+1], s[0], 10)
      db.draw_line_with_scale([x-s[0]/2-1, y], -10, s[1], rotate=True)
    if i == 4:
      db.draw_line_with_scale([x-s[0]/2, y+s[2]+s[1]-10], s[0], 0)
      db.draw_line_with_scale([x-s[0]/2+10, y+s[2]], 0, s[1], rotate=True)
  db.draw_text([x+ss[0][0]/5, y+ss[-1][2]+6.5], 'Rubber sheet')
  db.draw_text([x+ss[0][0]/5, y+ss[-1][2]+1.5], '(t=1)')
  ''' M3 hole '''
  for i in range(6):
    db.draw_circle([x-73.2*scale*(2.5-i), y+15*scale],
                   r=1.5*scale, lw=line_width)
    db.draw_circle([x-73.2*scale*(2.5-i), y+(15+371)*scale],
                   r=1.5*scale, lw=line_width)
    if i > 0 and i < 5:
      db.draw_circle([x-73.2*scale*2.5, y+15*scale+74.2*scale*i],
                     r=1.5*scale, lw=line_width)
      db.draw_circle([x+73.2*scale*2.5, y+15*scale+74.2*scale*i],
                     r=1.5*scale, lw=line_width)
  ''' M10+20 hole '''
  hole = [0, 425*scale, 10*scale]
  db.draw_circle([x, y+hole[1]],
                 r=hole[2], lw=line_width)
  db.draw_circle([x, y+hole[1]],
                 r=hole[2]/2, lw=line_width)
  ''' valve/pin '''
  valve = [12*scale, 15*scale]
  db.draw_square([x-valve[0]/2, y-valve[1]],
                 valve[0], valve[1], line_width=line_width)
  db.draw_arrow([x, y-valve[1]+1], 0, -2, 3)
  db.draw_text([x, y-valve[1]-4], 'Vacuum valve')
  leg_block = [40*scale, 5*scale, 20*scale]
  leg_pin = [75*scale, 5*scale]
  db.draw_square([x-ss[0][0]/2+leg_pin[0]-leg_block[0]/2,
                  y-leg_block[1]],
                 leg_block[0], leg_block[1], line_width=line_width)
  db.draw_square([x+ss[0][0]/2-leg_pin[0]-leg_block[0]/2,
                  y-leg_block[1]],
                 leg_block[0], leg_block[1], line_width=line_width)
  db.draw_polygon([x-ss[0][0]/2+leg_pin[0]-leg_pin[1]/2, y-leg_block[1]],
                  [[leg_pin[1]/2, -leg_pin[1]/2*math.sqrt(3)],
                   [leg_pin[1]/2, leg_pin[1]/2*math.sqrt(3)]],
                  line_width=line_width)
  db.draw_polygon([x+ss[0][0]/2-leg_pin[0]-leg_pin[1]/2, y-leg_block[1]],
                  [[leg_pin[1]/2, -leg_pin[1]/2*math.sqrt(3)],
                   [leg_pin[1]/2, leg_pin[1]/2*math.sqrt(3)]],
                  line_width=line_width)
  db.draw_arrow([x+ss[0][0]/2-leg_pin[0],
                 y-leg_block[1]-leg_pin[1]/2*math.sqrt(3)], 2, -2, 3)
  db.draw_text([x+ss[0][0]/2-leg_pin[0]+14, y-valve[1]-4],
               'Fixing pin')
  ''' beam mark '''
  db.draw_text([x-7, y+ss[0][1]/2-6.5], 'Beam')
  db.draw_circle([x+5, y+ss[0][1]/2-5],
                 r=20*scale, lw=line_width)
  db.draw_circle([x+5, y+ss[0][1]/2-5],
                 r=5*scale, lw=line_width, fc=0)
  '''
  side view
  '''
  x += ss[0][1]/2 + 30
  t = [9*scale, 20*scale]
  db.draw_polygon([x, y], [[t[1], 0],
                           [0, ss[1][1]],
                           [-t[1]+t[0], 0],
                           [0, ss[0][1]-ss[1][1]],
                           [-t[0], 0]], line_width=line_width)
  db.draw_line_with_scale([x, y+ss[0][1]+1], t[1], 10)
  db.draw_line_with_scale([x, y+ss[0][1]-6], t[0], 0)
  #print('[1 1] 0 setdash')
  db.draw_polygon([x, y+hole[1]+hole[2]], [[t[0]-1*scale, 0],
                                           [0, -hole[2]/2],
                                           [1*scale, 0],
                                           [0, -hole[2]],
                                           [-1*scale, 0],
                                           [0, -hole[2]/2],
                                           [-t[0]+1*scale, 0]],
                  line_width=line_width)
  ''' valve/pin '''
  db.draw_square([x+t[1]/2-valve[0]/2, y-valve[1]],
                 valve[0], valve[1], line_width=line_width)
  db.draw_square([x+t[1]/2-leg_block[2]/2,
                  y-leg_block[1]],
                 leg_block[2], leg_block[1], line_width=line_width)
  db.draw_polygon([x+t[1]/2-leg_pin[1]/2, y-leg_block[1]],
                  [[leg_pin[1]/2, -leg_pin[1]/2*math.sqrt(3)],
                   [leg_pin[1]/2, leg_pin[1]/2*math.sqrt(3)]],
                  line_width=line_width)
  ''' beam mark '''
  db.draw_text([x+ss[0][2]+13, y+ss[0][1]/2-3], 'Beam')
  db.draw_arrow([x-5, y+ss[0][1]/2-5], t[1]+10, 0, 2)
  ''' SUS '''
  db.draw_text([x-15, y+ss[0][1]-15], 'SUS foil')
  db.draw_text([x-15, y+ss[0][1]-20], '(t=0.1)')
  db.draw_arrow([x, y+ss[0][1]-13.5], -5, 0, 3)
  ''' unit '''
  db.draw_text([x+t[1]+20, y], '[mm]')
