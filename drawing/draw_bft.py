#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
import settings

#_______________________________________________________________________________
def draw():
  scale = 12.0
  settings.set_scale(scale)
  phi = 1.0*scale
  d = phi*math.sqrt(3)/2
  n = 20
  xcenter = settings.a4size[0]/2
  ycenter = settings.a4size[1]/2
  for i in range(n):
    if i == n/2 or i == n/2-1 or i == n/2+1 or i == n/2-2:
      continue
    db.draw_circle([xcenter+phi*i/2-phi*(n/4-0.25), ycenter + d*(i%2)], phi/2)
  db.draw_text([xcenter, ycenter+d/2], '...', False, 10)
  db.draw_text([xcenter, ycenter-phi-10-2.5], 'Upstream')
  db.draw_text([xcenter, ycenter+d+phi+10], 'Downstream')
  db.draw_line_with_scale([xcenter-phi*(n+1)/4, ycenter-phi/2], phi, -10)
