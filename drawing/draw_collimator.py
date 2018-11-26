#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
from settings import a4size, line_width
import settings

version = 2017

#_______________________________________________________________________________
def draw():
  scale = 0.2
  settings.set_scale(scale)
  t = 400*scale
  t_tan = 200*scale
  width = 400*scale
  w_tan = 140*scale
  height = [30*scale, 40*scale]
  if version == 2016:
    open_tan = [120*scale, 110*scale]
  elif version == 2017:
    open_tan = [180*scale, 160*scale]
  else:
    Exception('No such version: {}'.format(version))
  gap_tan = [(width-w_tan*2-open_tan[0])/2, (width-w_tan*2-open_tan[1])/2,]
  lead = [100*scale, 50*scale, 200*scale, 0.8]
  fcolor = 0.95
  unit_position = [a4size[0]-100*scale+open_tan[0], a4size[1]/2-20]
  db.draw_text(unit_position, '[mm]')
  # front view
  xoffset = (a4size[0]-width)/2-45
  yoffset = a4size[1]/2 + t_tan - height[0]/2 - height[1]
  db.draw_square([xoffset, yoffset], width, height[1], line_width, fcolor)
  db.draw_square([xoffset+gap_tan[1], yoffset+height[1]], w_tan, height[0], line_width, fcolor)
  db.draw_square([xoffset+gap_tan[0], yoffset+height[1]], w_tan, height[0], line_width, fcolor)
  db.draw_square([xoffset+width-gap_tan[1], yoffset+height[1]], -w_tan, height[0], line_width, fcolor)
  db.draw_square([xoffset+width-gap_tan[0], yoffset+height[1]], -w_tan, height[0], line_width, fcolor)
  db.draw_square([xoffset, yoffset+height[0]+height[1]], width, height[1], line_width, fcolor)
  for i in range(8):
    db.draw_square([xoffset+(i%4)*lead[0], yoffset+height[0]+height[1]*2+int(i/4)*lead[1]],
                lead[0], lead[1], line_width, lead[3])
    db.draw_square([xoffset+(i%4)*lead[0], yoffset-int(1+i/4)*lead[1]],
                lead[0], lead[1], line_width, lead[3])
  #db.draw_line_with_scale([xoffset, yoffset-lead[1]*2], width, -10)
  db.draw_line_with_scale([xoffset, yoffset+lead[1]*2+height[0]+height[1]*2], width, 8)
  db.draw_line_with_scale([xoffset, yoffset-lead[1]], -4, lead[1], True)
  db.draw_line_with_scale([xoffset, yoffset], -4, height[1], True)
  db.draw_line_with_scale([xoffset+gap_tan[0], yoffset+height[1]], -4, height[0], True)
  db.draw_line_with_scale([xoffset, yoffset-lead[1]*2], -18+gap_tan[0],
                       height[0]+height[1]*2+lead[1]*4, True)
  # db.draw_text([xoffset+width/2, 260], 'Front view', False, 6 )
  db.draw_text([xoffset+6.5, yoffset-lead[1]*2+1.5], 'Lead')
  db.draw_beam_mark([xoffset+width/2, yoffset-lead[1]*2-10], 5)
  db.draw_text([xoffset+width/2-12, yoffset-lead[1]*2-11.5], 'Beam')
  db.draw_text([xoffset, 245], '(b)', text_size=7)
  # cross-sectional view
  xoffset = (a4size[0]-width)/2+open_tan[0]+40
  yoffset = a4size[1]/2
  db.draw_square([xoffset, yoffset], width, t, line_width, fcolor)
  db.draw_square([xoffset+gap_tan[0], yoffset], w_tan, t_tan, line_width, fcolor)
  db.draw_square([xoffset+width-w_tan-gap_tan[0], yoffset], w_tan, t_tan, line_width, fcolor)
  db.draw_square([xoffset+gap_tan[1], yoffset+t_tan], w_tan, t_tan, line_width, fcolor)
  db.draw_square([xoffset+width-w_tan-gap_tan[1], yoffset+t_tan], w_tan, t_tan, line_width, fcolor)
  # db.draw_line_with_scale([xoffset, yoffset], width, -20)
  db.draw_line_with_scale([xoffset, yoffset], -4+gap_tan[0], t_tan, True)
  db.draw_line_with_scale([xoffset, yoffset+t_tan], -4+gap_tan[0], t_tan, True)
  db.draw_line_with_scale([xoffset, yoffset], -15+gap_tan[0], t, True)
  db.draw_line_with_scale([xoffset+gap_tan[0], yoffset], w_tan, -10)
  db.draw_line_with_scale([xoffset+w_tan+gap_tan[0], yoffset], open_tan[0], -10)
  db.draw_line_with_scale([xoffset+w_tan+gap_tan[1], yoffset+t], open_tan[1], 5)
  db.draw_text([xoffset+11+gap_tan[0], yoffset+1.5], 'Tungsten')
  db.draw_arrow([xoffset+width/2, yoffset+15], 0, t-30, 2)
  db.draw_text([xoffset+width/2+4, yoffset+t/2], 'Beam', rotate=True)
  # db.draw_text([xoffset+width/2, yoffset+t+15], 'Downstream')
  # db.draw_text([xoffset+width/2, yoffset-20], 'Upstream')
  # db.draw_text([xoffset+width/2, 260], 'Cross-sectional top view', False, 6)

#_______________________________________________________________________________
def set_version(ver):
  global version
  version = ver
