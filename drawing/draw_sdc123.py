#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import draw_basic as db
import settings

#_______________________________________________________________________________
def draw(scale, wire_spacing, shield_wire=None, track=False, abc_label=True):
  settings.set_scale(scale)
  r = wire_spacing/math.sqrt(3)
  width = wire_spacing*4
  xcenter = settings.a4size[0]/2
  ycenter = settings.a4size[1]/2 - wire_spacing
  n = int(width/wire_spacing)+1
  for i in range(8):
    for w in range(n):
      x = xcenter-width/2+(w+0.5*(i%2))*wire_spacing
      y = ycenter+i*r*0.5
      if i%3 == 0:
        db.draw_line([x, y], wire_spacing/2, r/2)
      if i%3 == 1:
        db.draw_line([x, y], wire_spacing/2, -r/2)
        if i != 7:
          db.draw_line([x, y], 0, r)
  for i in range(8):
    for w in range(n):
      x = xcenter-width/2+(w+0.5*(i%2))*wire_spacing
      y = ycenter+i*r*0.5
      db.draw_circle([x, y], 1, 0 if i%3 == 2 else 1.0)
      if settings.target == 'SDC3' and i%3 == 2:
        x = xcenter-width/2+(w+0.5*((i+1)%2))*wire_spacing
        db.draw_circle([x, y], 1, 1)
  db.draw_text([xcenter+width/2+wire_spacing/2+4, ycenter+3.5*r-1],
               'Potential wire', centering=False)
  db.draw_text([xcenter+width/2+wire_spacing/2+4, ycenter+2.5*r-1],
               'Anode wire', centering=False)
  db.draw_line_with_scale([xcenter-width/2, ycenter-1], wire_spacing, -4)
  db.draw_line_with_scale([xcenter-width/2+wire_spacing, ycenter-1],
                          wire_spacing/2, -4)
  db.draw_line_with_scale([xcenter-width/2-1, ycenter], -4, r, True)
  db.draw_line_with_scale([xcenter-width/2-1, ycenter+r], -4, 1.5*r, True)
  if shield_wire is not None:
    for i in range(2):
      for w in range(int(width/shield_wire[0])+1):
        x = xcenter-width/2+wire_spacing/4+w*shield_wire[0]
        y = ycenter - shield_wire[1]
        if i == 1: y += 3.5*r + 2*shield_wire[1]
        db.draw_circle([x, y], 1, 0.7)
    db.draw_line_with_scale([xcenter-width/2+wire_spacing/4,
                             ycenter+3.5*r+shield_wire[1]+1],
                            shield_wire[0], 4)
    db.draw_line_with_scale([xcenter-width/2+wire_spacing/4-1,
                             ycenter+3.5*r],
                            -4, shield_wire[1], True)
    db.draw_text([xcenter+width/2+wire_spacing/4+4,
                  ycenter+3.5*r+shield_wire[1]-1],
                  #ycenter-shield_wire[1]-1],
                 'Shield wire', centering=False)
    # db.draw_text([xcenter+width/2+r*3.5, ycenter-shield_wire[1]-6], '[mm]')
  else:
    pass
    # db.draw_text([xcenter+width/2+r*3.5, ycenter-wire_spacing/2], '[mm]')
  if track:
    db.draw_text([xcenter+wire_spacing/4+22, ycenter+r*4.5], 'Charged particle')
    db.draw_arrow([xcenter+wire_spacing/8, ycenter-r], wire_spacing/4, 5.5*r, 2)
    db.draw_text([xcenter+r, ycenter+2.5*r+7.5], 'Drift', False, 4)
    db.draw_text([xcenter+r, ycenter+2.5*r+3.5], 'length', False, 4)
    db.draw_text([xcenter-0.5, ycenter+r+7.5], 'Drift', False, 4)
    db.draw_text([xcenter-0.5, ycenter+r+3.5], 'length', False, 4)
    length = math.sqrt(pow(5.5*r, 2) + pow(wire_spacing/4, 2))/(1.05*scale)
    normal_vector = [5.5*r/length, -wire_spacing/4/length]
    db.draw_arrow([xcenter+0.25*wire_spacing+0.2*scale, ycenter+2.5*r+0.1*scale],
               normal_vector[0], normal_vector[1])
    db.draw_arrow([xcenter+1+0.01*scale, ycenter+r-0.01*scale],
               normal_vector[0], normal_vector[1])
  if abc_label:
    db.draw_text([xcenter-width/2-wire_spacing, ycenter+r*4.5],
                 ('(a)' if settings.target == 'SDC1' else
                  '(b)' if settings.target == 'SDC2' else '(c)'))

#_______________________________________________________________________________
def draw_sdc1():
  scale = 4.0
  wire_spacing = 6*scale
  shield_wire = [wire_spacing, (20*scale-3.5*wire_spacing/math.sqrt(3))/2]
  draw(scale, wire_spacing, shield_wire)

#_______________________________________________________________________________
def draw_sdc2():
  scale = 24/9
  wire_spacing = 9*scale
  shield_wire = [wire_spacing, (10-7/4*6/math.sqrt(3))*scale]
  draw(scale, wire_spacing, shield_wire)

#_______________________________________________________________________________
def draw_sdc3():
  scale=24/20
  wire_spacing = 20*scale
  shield_wire = [2*wire_spacing, 6*scale]
  draw(scale, wire_spacing, shield_wire)
